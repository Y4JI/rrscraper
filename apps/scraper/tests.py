from io import StringIO
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase

from .models import Chapter, ChapterRelease, Job, Novel
from .royalroad import RoyalRoadError


FICTION_URL = "https://www.royalroad.com/fiction/139212/the-hundred-reigns-timeloop-litrpg"
FICTION_HTML = b"""
<div class="fic-header">
  <h1>The Hundred Reigns [Timeloop LitRPG]</h1>
  <h4><a>Maxime J. Durand (Void Herald)</a></h4>
</div>
<table id="chapters">
  <tr><td><a href="/fiction/139212/story/chapter/1/first">First</a></td></tr>
  <tr class="chapter-row" data-url="/fiction/139212/story/chapter/2/second"><td>Second</td></tr>
</table>
"""
CHAPTER_HTML = b'''<h1>Site heading</h1><div class="fic-header"><h1>Sample chapter</h1></div>
<div class="chapter-content"><p>Sample <em>text</em>.</p><p>Another paragraph.</p></div>'''


class ImportNovelTests(TestCase):
    def setUp(self):
        get_user_model().objects.create_user(username="reader")

    def run_import(self):
        call_command("import_novel", FICTION_URL, username="reader", stdout=StringIO())

    @patch("apps.scraper.importer.fetch_page")
    def test_rss_import_saves_release_metadata_without_creating_chapters(self, fetch):
        fetch.return_value = b"""\xef\xbb\xbf<rss><channel><title>The Hundred Reigns</title>
          <item><title>The Hundred Reigns - First chapter</title>
            <link>https://www.royalroad.com/fiction/chapter/123</link>
            <pubDate>Tue, 24 Nov 2026 15:00:00 GMT</pubDate>
            <description>A teaser is not a chapter.</description></item>
          <item><title>Offsite</title><link>https://example.com/fiction/chapter/456</link></item>
          <item><title>Other fiction</title><link>https://www.royalroad.com/fiction/1/story/chapter/456</link></item>
        </channel></rss>"""
        for _ in range(2):
            call_command("import_novel", FICTION_URL, username="reader", rss=True, stdout=StringIO())
        self.assertEqual(Novel.objects.get(royalroad_id="139212").title, "The Hundred Reigns")
        release = ChapterRelease.objects.get()
        self.assertEqual(release.title, "First chapter")
        self.assertEqual(release.royalroad_chapter_id, "123")
        self.assertEqual(release.release_date.day, 24)
        self.assertFalse(Chapter.objects.exists())
        self.assertEqual(Job.objects.filter(
            source=Job.Source.RSS, status="COMPLETED", releases_imported=1, chapters_scraped=0,
        ).count(), 2)

    @patch("apps.scraper.importer.fetch_page")
    def test_author_export_imports_complete_text_without_network(self, fetch):
        export = {
            "royalroad_id": "139212", "title": "Authorized novel", "author_name": "Test author",
            "chapters": [{
                "source_url": f"{FICTION_URL}/chapter/123/first", "chapter_number": 1,
                "title": "First", "content": "Complete test body.",
            }],
        }
        with TemporaryDirectory() as directory:
            path = Path(directory) / "export.json"
            path.write_text(json.dumps(export), encoding="utf-8")
            for _ in range(2):
                call_command("import_novel", FICTION_URL, username="reader", author_export=str(path), stdout=StringIO())
            export["chapters"][0]["source_url"] = "https://www.royalroad.com/fiction/1/other/chapter/123/first"
            path.write_text(json.dumps(export), encoding="utf-8")
            with self.assertRaisesMessage(CommandError, "belong to the exported novel"):
                call_command("import_novel", FICTION_URL, username="reader", author_export=str(path), stdout=StringIO())
        fetch.assert_not_called()
        self.assertEqual(Chapter.objects.get().content, "Complete test body.")
        self.assertEqual(Job.objects.filter(source=Job.Source.AUTHOR, status="COMPLETED").count(), 2)
        self.assertEqual(Job.objects.first().status, "FAILED")

    @patch("apps.scraper.importer.sleep")
    @patch("apps.scraper.importer.fetch_page")
    def test_repeat_import_updates_without_duplicates(self, fetch, sleep):
        fetch.side_effect = [FICTION_HTML, CHAPTER_HTML, CHAPTER_HTML] * 2
        self.run_import()
        self.run_import()
        self.assertEqual(Novel.objects.get().title, "The Hundred Reigns [Timeloop LitRPG]")
        self.assertEqual(list(Chapter.objects.values_list("chapter_number", flat=True)), [1, 2])
        first_chapter = Chapter.objects.get(chapter_number=1)
        self.assertEqual(first_chapter.title, "Sample chapter")
        self.assertEqual(first_chapter.content, "Sample text.\nAnother paragraph.")
        self.assertEqual(Job.objects.filter(status="COMPLETED", chapters_scraped=2).count(), 2)

    @patch("apps.scraper.importer.sleep")
    @patch("apps.scraper.importer.fetch_page")
    def test_failed_job_keeps_saved_chapter(self, fetch, sleep):
        fetch.side_effect = [FICTION_HTML, CHAPTER_HTML, RoyalRoadError("HTTP 403")]
        with self.assertRaisesMessage(CommandError, "HTTP 403"):
            self.run_import()
        self.assertEqual(Chapter.objects.get().chapter_number, 1)
        self.assertEqual(Job.objects.get().status, "FAILED")
        self.assertEqual(Job.objects.get().chapters_scraped, 1)
