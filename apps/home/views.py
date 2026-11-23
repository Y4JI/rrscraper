from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render

from apps.scraper.importer import import_novel
from apps.scraper.models import Chapter, Job, Novel
from apps.scraper.royalroad import RoyalRoadError

from .forms import NovelImportForm


@login_required
def home_view(request):
    import_form = NovelImportForm()
    if request.method == "POST":
        import_form = NovelImportForm(request.POST)
        if import_form.is_valid():
            try:
                job = import_novel(
                    import_form.cleaned_data["fiction_url"], request.user, 0, from_rss=True
                )
            except RoyalRoadError:
                messages.error(request, "The Royal Road import failed. See the latest import for details.")
            else:
                messages.success(request, f"Saved {job.novel.title} from Royal Road RSS.")
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
        results = library[:5]

    return render(request, "home/home.html", {
        "novel_count": library.count(),
        "chapter_count": Chapter.objects.count(),
        "latest_job": Job.objects.filter(user=request.user).order_by("-started_at", "-pk").first(),
        "recent_novels": results,
        "library_query": library_query,
        "import_form": import_form,
    })

