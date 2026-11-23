from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_GET

from apps.profile.models import Profile
from apps.scraper.importer import enqueue_rss
from apps.scraper.models import Chapter, Job, Novel
from apps.scraper.royalroad import RoyalRoadError
from apps.scraper.worker import worker_is_online

from .forms import NovelImportForm


def import_status_context(user):
    return {
        "latest_job": Job.objects.filter(user=user).select_related("novel").order_by("-pk").first(),
        "worker_online": worker_is_online(),
    }


@login_required
@require_GET
@never_cache
def import_status(request):
    return render(request, "home/import_status.html", import_status_context(request.user))


@login_required
def home_view(request):
    import_form = NovelImportForm()
    if request.method == "POST":
        import_form = NovelImportForm(request.POST)
        if import_form.is_valid():
            try:
                _, created = enqueue_rss(import_form.cleaned_data["fiction_url"], request.user)
            except RoyalRoadError:
                messages.error(request, "The Royal Road import failed. See the latest import for details.")
            else:
                if created:
                    messages.success(request, "Import queued.")
                else:
                    messages.info(request, "An import for this novel is already in progress. Check the library after it finishes.")
            return redirect("home:home")

    library_query = request.GET.get("q", "").strip()[:255]
    library = Novel.objects.order_by("-updated_at", "-pk")
    if library_query:
        results = library.filter(
            Q(title__icontains=library_query)
            | Q(author_name__icontains=library_query)
            | Q(tags__name__icontains=library_query)
        ).distinct()
    else:
        results = library
    library_page = Paginator(results, 10).get_page(request.GET.get("page"))
    display_name = Profile.objects.filter(user=request.user).values_list("full_name", flat=True).first()

    return render(request, "home/home.html", {
        "novel_count": library.count(),
        "chapter_count": Chapter.objects.count(),
        **import_status_context(request.user),
        "recent_novels": library_page,
        "library_page": library_page,
        "display_name": display_name or request.user.first_name or request.user.username,
        "library_query": library_query,
        "import_form": import_form,
    })

