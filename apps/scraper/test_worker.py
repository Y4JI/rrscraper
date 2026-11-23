from unittest.mock import patch
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone

from .importer import enqueue_rss
from .models import WorkerHeartbeat
from .royalroad import TemporaryRoyalRoadError
from .worker import worker_is_online


class WorkerTests(TestCase):
    @patch("apps.scraper.importer.fetch_page", side_effect=TemporaryRoyalRoadError("Unavailable"))
    def test_temporary_failure_retries_three_times(self, fetch):
        user = get_user_model().objects.create_user(username="retry-reader")
        job, _ = enqueue_rss("https://www.royalroad.com/fiction/139212/story", user)
        for attempt in range(1, 4):
            call_command("process_imports", once=True)
            job.refresh_from_db()
            self.assertEqual(job.attempts, attempt)
            if attempt < 3:
                self.assertEqual(job.status, "PENDING")
                self.assertIsNotNone(job.active_key)
                self.assertGreater(job.retry_at, timezone.now())
                call_command("process_imports", once=True)
                self.assertEqual(fetch.call_count, attempt)
                type(job).objects.filter(pk=job.pk).update(retry_at=timezone.now() - timedelta(seconds=1))
        self.assertEqual(job.status, "FAILED")
        self.assertIsNone(job.active_key)

    def test_stale_heartbeat_is_offline(self):
        self.assertFalse(worker_is_online())
        WorkerHeartbeat.objects.create(name="rss", last_seen=timezone.now())
        self.assertTrue(worker_is_online())
        WorkerHeartbeat.objects.update(last_seen=timezone.now() - timedelta(seconds=61))
        self.assertFalse(worker_is_online())
