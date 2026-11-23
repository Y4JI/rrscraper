from datetime import timedelta

from django.utils import timezone

from .models import WorkerHeartbeat


def worker_is_online():
    return WorkerHeartbeat.objects.filter(
        name="rss", last_seen__gte=timezone.now() - timedelta(seconds=60)
    ).exists()
