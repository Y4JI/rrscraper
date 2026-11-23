from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from apps.scraper.models import ChapterRelease, Novel
from .models import Bookmark


class ShelfTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user("shelf-reader")
        self.other = get_user_model().objects.create_user("other-reader")
        self.novel = Novel.objects.create(royalroad_id="1", title="Shelf story", source_url="https://www.royalroad.com/fiction/1/story")
        self.client.force_login(self.user)

    def test_unfollow_preserves_progress_and_favorite(self):
        bookmark = Bookmark.objects.create(user=self.user, novel=self.novel, is_favorite=True)
        self.client.post(reverse("tracker:follow", args=[self.novel.pk]), {"action": "unfollow"})
        bookmark.refresh_from_db()
        self.assertFalse(bookmark.is_following)
        self.assertTrue(bookmark.is_favorite)
        self.assertNotContains(self.client.get(reverse("tracker:shelf")), self.novel.title)

    def test_shelf_is_private_and_only_new_releases_count(self):
        bookmark = Bookmark.objects.create(user=self.user, novel=self.novel)
        ChapterRelease.objects.create(novel=self.novel, royalroad_chapter_id="2", title="Old", source_url="https://www.royalroad.com/fiction/chapter/2", release_date=timezone.now()-timedelta(days=1))
        ChapterRelease.objects.create(novel=self.novel, royalroad_chapter_id="3", title="New", source_url="https://www.royalroad.com/fiction/chapter/3", release_date=timezone.now()+timedelta(seconds=1))
        response = self.client.get(reverse("tracker:shelf"))
        self.assertContains(response, "1 new release")
        self.client.force_login(self.other)
        self.assertNotContains(self.client.get(reverse("tracker:shelf")), self.novel.title)

    def test_follow_requires_post(self):
        self.assertEqual(self.client.get(reverse("tracker:follow", args=[self.novel.pk])).status_code, 405)

    def test_newer_releases_remain_unread_after_marking_an_older_release(self):
        published = timezone.now() - timedelta(days=2)
        older = ChapterRelease.objects.create(
            novel=self.novel, royalroad_chapter_id="2", title="Older",
            source_url="https://www.royalroad.com/fiction/chapter/2", release_date=published,
        )
        ChapterRelease.objects.create(
            novel=self.novel, royalroad_chapter_id="3", title="Newer",
            source_url="https://www.royalroad.com/fiction/chapter/3", release_date=published + timedelta(days=1),
        )
        self.client.post(reverse("tracker:mark_read", args=[self.novel.pk, "release", older.pk]))
        self.assertContains(self.client.get(reverse("tracker:shelf")), "1 new release")
