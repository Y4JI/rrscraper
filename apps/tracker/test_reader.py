from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from apps.scraper.models import Chapter, Novel
from .models import Bookmark


class ReaderNavigationTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="reader")
        self.novel = Novel.objects.create(royalroad_id="123", title="Sample", source_url="https://www.royalroad.com/fiction/123/sample")
        self.chapters = [Chapter.objects.create(novel=self.novel, royalroad_chapter_id=str(i), chapter_number=1, title=f"Part {i}", content="Sample body") for i in range(3)]
        self.client.force_login(self.user)

    def url(self, chapter):
        return reverse("tracker:chapter_detail", args=[self.novel.pk, chapter.pk])

    def test_navigation_handles_equal_numbers_and_boundaries(self):
        middle = self.client.get(self.url(self.chapters[1]))
        self.assertEqual(middle.context["previous_chapter"], self.chapters[0])
        self.assertEqual(middle.context["next_chapter"], self.chapters[2])
        self.assertIsNone(self.client.get(self.url(self.chapters[0])).context["previous_chapter"])
        self.assertIsNone(self.client.get(self.url(self.chapters[2])).context["next_chapter"])

    def test_save_progress_stays_in_reader_and_preserves_favorite(self):
        Bookmark.objects.create(user=self.user, novel=self.novel, is_favorite=True)
        response = self.client.post(self.url(self.chapters[1]), {"next": "https://example.com"})
        self.assertRedirects(response, self.url(self.chapters[1]))
        bookmark = Bookmark.objects.get(user=self.user, novel=self.novel)
        self.assertTrue(bookmark.is_favorite)
        self.assertEqual(bookmark.last_read_chapter, self.chapters[1])

    def test_save_progress_requires_csrf(self):
        client = Client(enforce_csrf_checks=True)
        client.force_login(self.user)
        self.assertEqual(client.post(self.url(self.chapters[0])).status_code, 403)
        self.assertFalse(Bookmark.objects.exists())
