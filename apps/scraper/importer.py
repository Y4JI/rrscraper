from time import sleep
from datetime import timedelta

from django.db import transaction
from django.utils import timezone

from .author_export import read_author_export
from .models import Chapter, ChapterRelease, Job, Novel
from .parsers import parse_chapter, parse_feed, parse_fiction
from .royalroad import CHAPTER_PATH, FICTION_PATH, RSS_PATH, RoyalRoadError, canonical_fiction, fetch_page
from .royalroad import TemporaryRoyalRoadError


def import_novel(url, user, max_chapters, *, from_rss=False, author_export=None, job=None):
    fiction_id, url = canonical_fiction(url)
    if from_rss and author_export is not None:
        raise RoyalRoadError("Choose one import source.")
    source = Job.Source.WEB
    if from_rss:
        source = Job.Source.RSS
    elif author_export is not None:
        source = Job.Source.AUTHOR
    job = job or Job.objects.create(user=user, target_url=url, status="RUNNING", source=source)
    try:
        if from_rss:
            feed_url = f"https://www.royalroad.com/fiction/syndication/{fiction_id}"
            feed = fetch_page(feed_url, RSS_PATH, ("text/xml", "application/xml", "application/rss+xml"))
            title, releases = parse_feed(feed, fiction_id)
            with transaction.atomic():
                novel = save_novel(fiction_id, {"title": title, "source_url": url})
                for chapter_id, release in releases.items():
                    ChapterRelease.objects.update_or_create(
                        novel=novel, royalroad_chapter_id=chapter_id, defaults=release,
                    )
            job.novel = novel
            job.releases_imported = len(releases)
        elif author_export is not None:
            metadata, chapters = read_author_export(author_export, fiction_id)
            with transaction.atomic():
                novel = save_novel(fiction_id, {**metadata, "source_url": url})
                for chapter_id, chapter in chapters.items():
                    Chapter.objects.update_or_create(
                        novel=novel, royalroad_chapter_id=chapter_id, defaults=chapter,
                    )
            job.novel = novel
            job.chapters_scraped = len(chapters)
        else:
            import_website(job, fiction_id, url, max_chapters)
    except (Exception, KeyboardInterrupt) as exc:
        job.status = "FAILED"
        job.error_message = str(exc) or "Import interrupted."
        if isinstance(exc, TemporaryRoyalRoadError) and job.active_key and job.attempts < 3:
            job.status = "PENDING"
            job.retry_at = timezone.now() + timedelta(seconds=30 * 2 ** max(job.attempts - 1, 0))
        raise
    else:
        job.status = "COMPLETED"
    finally:
        job.completed_at = timezone.now()
        if job.status != "PENDING":
            job.active_key = None
            job.retry_at = None
        else:
            job.completed_at = None
        job.save(update_fields=[
            "status", "error_message", "completed_at", "active_key", "retry_at", "novel", "chapters_scraped", "releases_imported",
        ])
    return job


def save_novel(fiction_id, metadata):
    novel, _ = Novel.objects.update_or_create(royalroad_id=fiction_id, defaults=metadata)
    return novel


def import_website(job, fiction_id, url, max_chapters):
    metadata, chapters = parse_fiction(fetch_page(url, FICTION_PATH), url)
    job.novel = save_novel(fiction_id, metadata)
    job.save(update_fields=["novel"])
    if max_chapters and not chapters:
        raise RoyalRoadError("No chapter links were found on the fiction page.")

    for number, (chapter_id, chapter_url) in enumerate(list(chapters.items())[:max_chapters], start=1):
        sleep(1)
        title, content = parse_chapter(fetch_page(chapter_url, CHAPTER_PATH))
        Chapter.objects.update_or_create(
            novel=job.novel,
            royalroad_chapter_id=chapter_id,
            defaults={
                "chapter_number": number,
                "title": title,
                "content": content,
                "word_count": len(content.split()),
                "source_url": chapter_url,
            },
        )
        job.chapters_scraped = number
        job.save(update_fields=["chapters_scraped"])


def enqueue_rss(url, user):
    fiction_id, url = canonical_fiction(url)
    job, created = Job.objects.get_or_create(
        active_key=fiction_id,
        defaults={"user": user, "target_url": url, "source": Job.Source.RSS},
    )
    return job, created
