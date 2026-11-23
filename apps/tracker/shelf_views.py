from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from apps.scraper.models import Novel
from .models import Bookmark
from .views import release_url


@login_required
def shelf(request):
    bookmarks = Bookmark.objects.filter(user=request.user, is_following=True).select_related(
        "novel", "last_read_chapter", "last_read_release"
    )
    page = Paginator(bookmarks, 10).get_page(request.GET.get("page"))
    entries = []
    for bookmark in page:
        resume = None
        last_release = None
        releases = bookmark.novel.releases.all()
        if bookmark.last_read_chapter and bookmark.last_read_chapter.novel_id == bookmark.novel_id:
            resume = reverse("tracker:chapter_detail", args=[bookmark.novel_id, bookmark.last_read_chapter_id])
            last_release = releases.filter(royalroad_chapter_id=bookmark.last_read_chapter.royalroad_chapter_id).first()
        elif bookmark.last_read_release and bookmark.last_read_release.novel_id == bookmark.novel_id:
            last_release = bookmark.last_read_release
            resume = release_url(last_release, bookmark.novel.royalroad_id)
        if last_release and last_release.release_date:
            newer_releases = releases.filter(
                Q(release_date__gt=last_release.release_date)
                | Q(release_date=last_release.release_date, pk__gt=last_release.pk)
            )
        else:
            baseline = bookmark.last_read_at if resume else bookmark.created_at
            newer_releases = releases.filter(release_date__gt=baseline)
        entries.append((bookmark, resume, newer_releases.count()))
    return render(request, "tracker/shelf.html", {"entries": entries, "page": page})


@login_required
@require_POST
def follow(request, novel_id):
    novel = get_object_or_404(Novel, pk=novel_id)
    action = request.POST.get("action")
    if action not in {"follow", "unfollow"}:
        return HttpResponseBadRequest("Choose follow or unfollow.")
    following = action == "follow"
    Bookmark.objects.update_or_create(user=request.user, novel=novel, defaults={"is_following": following})
    messages.success(request, "Following novel." if following else "Novel unfollowed. Your reading progress is saved.")
    return redirect("tracker:novel_detail", novel_id=novel.pk)
