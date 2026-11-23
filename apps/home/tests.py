from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from apps.scraper.models import Job, Novel, Tag
from apps.scraper.royalroad import RoyalRoadError


class DashboardTests(TestCase):
    fiction_url = "https://www.royalroad.com/fiction/139212/the-hundred-reigns-timeloop-litrpg"
    title = "The Hundred Reigns"

    def setUp(self):
        self.user = get_user_model().objects.create_user(username="reader")
        self.client.force_login(self.user)
        self.home = reverse("home:home")

    def test_search_matches_title_author_and_tags_without_duplicates(self):
        novel = Novel.objects.create(
            royalroad_id="139212",
            title=self.title,
            author_name="Maxime J. Durand",
            source_url=self.fiction_url,
        )
        novel.tags.add(
            Tag.objects.create(name="Fantasy", slug="fantasy"),
            Tag.objects.create(name="Progression Fantasy", slug="progression-fantasy"),
        )
        Novel.objects.create(royalroad_id="2", title="Other title", source_url=self.fiction_url)
        detail_url = reverse("tracker:novel_detail", kwargs={"novel_id": novel.pk})

        for term in ("hundred", "durand", "fantasy"):
            with self.subTest(term=term):
                response = self.client.get(self.home, {"q": term})
                self.assertContains(response, self.title, count=1)
                self.assertContains(response, f'href="{detail_url}"')
                self.assertNotContains(response, "Other title")
        self.assertContains(self.client.get(self.home, {"q": "missing"}), "No novels matched")

    def test_import_requires_login_and_csrf(self):
        response = Client().post(self.home, {"fiction_url": self.fiction_url})
        self.assertRedirects(response, f"{reverse('login:login')}?next={self.home}")
        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.force_login(self.user)
        self.assertEqual(csrf_client.post(self.home, {"fiction_url": self.fiction_url}).status_code, 403)

    @patch("apps.home.views.import_novel")
    def test_import_rejects_non_fiction_and_non_royal_road_urls(self, importer):
        for url in (
            "https://example.com/fiction/139212",
            "https://www.royalroad.com/fiction/chapter/10",
            "http://www.royalroad.com/fiction/139212",
        ):
            with self.subTest(url=url):
                response = self.client.post(self.home, {"fiction_url": url})
                self.assertContains(response, "Enter a Royal Road fiction URL.")
        importer.assert_not_called()

    @patch("apps.scraper.importer.fetch_page")
    def test_successful_import_redirects_to_rss_outcome(self, fetch):
        fetch.return_value = (
            b"<rss><channel><title>The Hundred Reigns</title></channel></rss>"
        )
        response = self.client.post(self.home, {"fiction_url": f"{self.fiction_url}?utm=test"})
        self.assertRedirects(response, self.home)
        novel = Novel.objects.get()
        self.assertEqual(novel.source_url, self.fiction_url)
        job = Job.objects.get(user=self.user)
        self.assertEqual(job.source, Job.Source.RSS)
        self.assertEqual(job.status, "COMPLETED")
        dashboard = self.client.get(self.home)
        self.assertContains(dashboard, "Title imported")
        self.assertContains(dashboard, "Royal Road RSS")
        self.assertContains(dashboard, "0 chapters downloaded")
        self.assertContains(dashboard, 'datetime="')

    @patch("apps.scraper.importer.fetch_page")
    def test_failed_import_shows_error_to_owner_only(self, fetch):
        fetch.side_effect = RoyalRoadError("Could not download releases.")
        response = self.client.post(self.home, {"fiction_url": self.fiction_url}, follow=True)
        self.assertContains(response, "Failed")
        self.assertContains(response, "Could not download releases.")
        self.assertEqual(Job.objects.get(user=self.user).status, "FAILED")

        other_user = get_user_model().objects.create_user(username="other-reader")
        self.client.force_login(other_user)
        response = self.client.get(self.home)
        self.assertContains(response, "Idle")
        self.assertNotContains(response, "Could not download releases.")
