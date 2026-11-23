from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from apps.scraper.models import Chapter, ChapterRelease, Novel

from .models import Bookmark


class TrackerTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.reader = get_user_model().objects.create_user(username="reader")
        cls.other_reader = get_user_model().objects.create_user(username="other-reader")
        cls.novel = Novel.objects.create(
            royalroad_id="10", title="A Royal Road Novel", source_url="https://www.royalroad.com/fiction/10"
        )
        cls.other_novel = Novel.objects.create(
            royalroad_id="11", title="Another Novel", source_url="https://www.royalroad.com/fiction/11"
        )
        cls.release = ChapterRelease.objects.create(
            novel=cls.novel,
            royalroad_chapter_id="20",
            title="First release",
            source_url="https://www.royalroad.com/fiction/chapter/20",
        )
        cls.chapter = Chapter.objects.create(
            novel=cls.novel, royalroad_chapter_id="20", chapter_number=1, title="Downloaded chapter",
            content="<script>alert(1)</script>\n\nSecond paragraph.",
            source_url=cls.release.source_url,
        )

    def setUp(self):
        self.client.force_login(self.reader)
        self.detail = reverse("tracker:novel_detail", args=[self.novel.pk])
        self.chapter_detail = reverse("tracker:chapter_detail", args=[self.novel.pk, self.chapter.pk])

    def test_release_history_exposes_older_saved_releases(self):
        for number in range(30, 42):
            ChapterRelease.objects.create(novel=self.novel, royalroad_chapter_id=str(number),
                title=f"Release {number}", source_url=f"https://www.royalroad.com/fiction/chapter/{number}")
        first = self.client.get(self.detail)
        second = self.client.get(self.detail, {"page": 2})
        self.assertEqual(len(first.context["releases"]), 10)
        self.assertEqual(len(second.context["releases"]), 3)
        self.assertContains(second, "First release")

    def test_public_cannot_view_reader(self):
        self.client.logout()
        self.assertRedirects(self.client.get(self.detail), f"{reverse('login:login')}?next={self.detail}")
        self.assertRedirects(
            self.client.get(self.chapter_detail), f"{reverse('login:login')}?next={self.chapter_detail}"
        )

    def test_novel_detail_shows_release_and_downloaded_chapter(self):
        response = self.client.get(self.detail)
        self.assertContains(response, self.novel.source_url)
        self.assertContains(response, self.release.source_url)
        self.assertContains(response, self.chapter_detail)

    def test_novel_detail_does_not_link_untrusted_release_url(self):
        ChapterRelease.objects.filter(pk=self.release.pk).update(source_url="https://example.org/bad-release")
        response = self.client.get(self.detail)
        self.assertContains(response, "First release")
        self.assertNotContains(response, "https://example.org/bad-release")

    def test_chapter_reader_escapes_text_and_rejects_mismatched_novel(self):
        response = self.client.get(self.chapter_detail)
        self.assertContains(response, "&lt;script&gt;alert(1)&lt;/script&gt;")
        self.assertNotContains(response, "<script>alert(1)</script>")
        self.assertEqual(self.client.get(reverse(
            "tracker:chapter_detail", args=[self.other_novel.pk, self.chapter.pk]
        )).status_code, 404)

    def test_mark_read_changes_only_current_readers_bookmark(self):
        other_bookmark = Bookmark.objects.create(user=self.other_reader, novel=self.novel, is_favorite=True)
        release_url = reverse("tracker:mark_read", args=[self.novel.pk, "release", self.release.pk])
        self.assertEqual(self.client.get(release_url).status_code, 405)
        self.assertRedirects(self.client.post(release_url), self.detail)
        bookmark = Bookmark.objects.get(user=self.reader, novel=self.novel)
        self.assertEqual(bookmark.last_read_release, self.release)
        self.assertContains(self.client.get(self.detail), "Last read")

        chapter_url = reverse("tracker:mark_read", args=[self.novel.pk, "chapter", self.chapter.pk])
        self.assertRedirects(self.client.post(chapter_url), self.detail)
        bookmark.refresh_from_db()
        self.assertEqual(bookmark.last_read_chapter, self.chapter)
        self.assertIsNone(bookmark.last_read_release)

        other_bookmark.refresh_from_db()
        self.assertTrue(other_bookmark.is_favorite)
        self.assertIsNone(other_bookmark.last_read_chapter)
        self.assertIsNone(other_bookmark.last_read_release)
        self.assertEqual(Bookmark.objects.filter(user=self.reader, novel=self.novel).count(), 1)

    def test_mark_read_rejects_release_from_another_novel(self):
        wrong_novel_url = reverse("tracker:mark_read", args=[self.other_novel.pk, "release", self.release.pk])
        self.assertEqual(self.client.post(wrong_novel_url).status_code, 404)
        self.assertFalse(Bookmark.objects.filter(user=self.reader).exists())

    def test_mark_read_requires_csrf_token(self):
        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.force_login(self.reader)
        release_url = reverse("tracker:mark_read", args=[self.novel.pk, "release", self.release.pk])
        self.assertEqual(csrf_client.post(release_url).status_code, 403)
        self.assertFalse(Bookmark.objects.filter(user=self.reader).exists())
