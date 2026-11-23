from time import monotonic, sleep

from django.core.management.base import BaseCommand
from django.db.models import F, Q
from django.utils import timezone

from apps.scraper.importer import import_novel
from apps.scraper.models import Job, WorkerHeartbeat


class Command(BaseCommand):
    help = "Process queued RSS imports. Run one worker per installation."

    def add_arguments(self, parser):
        parser.add_argument("--once", action="store_true", help="Process jobs that are due and exit.")
        parser.add_argument("--recover-job", type=int, help="Requeue a running job after stopping its old worker.")

    def handle(self, *args, **options):
        if options["recover_job"]:
            Job.objects.filter(pk=options["recover_job"], status="RUNNING", source=Job.Source.RSS).update(
                status="PENDING", error_message=None, completed_at=None, retry_at=None
            )
        next_heartbeat = 0
        while True:
            now = timezone.now()
            if not options["once"] and monotonic() >= next_heartbeat:
                WorkerHeartbeat.objects.update_or_create(name="rss", defaults={"last_seen": now})
                next_heartbeat = monotonic() + 10
            due = Job.objects.filter(status="PENDING", source=Job.Source.RSS).filter(
                Q(retry_at__isnull=True) | Q(retry_at__lte=now)
            )
            job = due.order_by("pk").first()
            if job is None:
                if options["once"]:
                    return
                sleep(2)
                continue
            claimed = due.filter(pk=job.pk).update(
                status="RUNNING", started_at=now, attempts=F("attempts") + 1,
                error_message=None, retry_at=None,
            )
            if not claimed:
                continue
            job.refresh_from_db()
            try:
                import_novel(job.target_url, job.user, 0, from_rss=True, job=job)
            except KeyboardInterrupt:
                raise
            except Exception as exc:
                self.stderr.write(f"Job {job.pk} failed: {exc}")
            else:
                self.stdout.write(f"Job {job.pk} completed: {job.releases_imported} releases synced.")
