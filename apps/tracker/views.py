from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import F, Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from apps.scraper.models import Chapter, ChapterRelease, Novel
from apps.scraper.royalroad import CHAPTER_PATH, FICTION_PATH, SHORT_CHAPTER_PATH, RoyalRoadError, identify

from .models import Bookmark


def release_url(release, fiction_id):
    try:
        matches = identify(release.source_url, SHORT_CHAPTER_PATH) == (release.royalroad_chapter_id,)
    except RoyalRoadError:
        try:
            matches = identify(release.source_url, CHAPTER_PATH) == (fiction_id, release.royalroad_chapter_id)
        except RoyalRoadError:
            return None
    return release.source_url if matches else None


@login_required
def novel_detail(request, novel_id):
    novel = get_object_or_404(Novel, pk=novel_id)
    bookmark = Bookmark.objects.filter(user=request.user, novel=novel).select_related(
        "last_read_chapter", "last_read_release"
    ).first()
    try:
        valid_source = identify(novel.source_url, FICTION_PATH) == (novel.royalroad_id,)
    except RoyalRoadError:
        valid_source = False
    releases = novel.releases.order_by(F("release_date").desc(nulls_last=True), "-pk")
    release_page = Paginator(releases, 10).get_page(request.GET.get("page"))

    return render(request, "tracker/novel_detail.html", {
        "novel": novel,
        "last_sync": novel.scraper_jobs.filter(source="RSS", status="COMPLETED").order_by("-completed_at").first(),
        "source_url": novel.source_url if valid_source else None,
        "releases": [(release, release_url(release, novel.royalroad_id)) for release in release_page],
        "release_page": release_page,
        "chapters": novel.chapters.defer("content"),
        "bookmark": bookmark,
    })


@login_required
def chapter_detail(request, novel_id, chapter_id):
    chapter = get_object_or_404(Chapter.objects.select_related("novel"), pk=chapter_id, novel_id=novel_id)
    if request.method == "POST":
        Bookmark.objects.update_or_create(
            user=request.user, novel_id=novel_id,
            defaults={"last_read_chapter": chapter, "last_read_release": None, "last_read_at": timezone.now()},
        )
        messages.success(request, "Reading progress saved.")
        return redirect("tracker:chapter_detail", novel_id=novel_id, chapter_id=chapter_id)
    chapters = Chapter.objects.filter(novel_id=novel_id).defer("content")
    previous_chapter = chapters.filter(
        Q(chapter_number__lt=chapter.chapter_number)
        | Q(chapter_number=chapter.chapter_number, pk__lt=chapter.pk)
    ).order_by("-chapter_number", "-pk").first()
    next_chapter = chapters.filter(
        Q(chapter_number__gt=chapter.chapter_number)
        | Q(chapter_number=chapter.chapter_number, pk__gt=chapter.pk)
    ).order_by("chapter_number", "pk").first()
    return render(request, "tracker/chapter_detail.html", {
        "chapter": chapter, "previous_chapter": previous_chapter, "next_chapter": next_chapter,
    })


@login_required
@require_POST
def mark_read(request, novel_id, entry_type, entry_id):
    entries = {"chapter": Chapter, "release": ChapterRelease}
    model = entries.get(entry_type)
    if model is None:
        raise Http404
    entry = get_object_or_404(model, novel_id=novel_id, pk=entry_id)
    Bookmark.objects.update_or_create(
        user=request.user,
        novel_id=novel_id,
        defaults={
            "last_read_chapter": entry if entry_type == "chapter" else None,
            "last_read_release": entry if entry_type == "release" else None,
            "last_read_at": timezone.now(),
        },
    )
    messages.success(request, "Reading progress saved.")
    return redirect("tracker:novel_detail", novel_id=novel_id)
