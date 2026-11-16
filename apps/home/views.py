from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.scraper.models import Novel, Chapter, Job


@login_required(login_url='login:login')
def home_view(request):
    """Renders the main home screen (protected) with live DB stats."""
    novel_count = Novel.objects.count()
    chapter_count = Chapter.objects.count()
    latest_job = Job.objects.filter(user=request.user).first() or Job.objects.first()
    scraper_status = latest_job.status if latest_job else "Idle"

    context = {
        'novel_count': novel_count,
        'chapter_count': chapter_count,
        'scraper_status': scraper_status,
        'recent_novels': Novel.objects.all()[:5],
    }
    return render(request, 'home/home.html', context)

