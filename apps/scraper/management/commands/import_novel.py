from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from ...importer import import_novel
from ...royalroad import RoyalRoadError


class Command(BaseCommand):
    help = "Import a Royal Road fiction and up to the requested number of chapters."

    def add_arguments(self, parser):
        parser.add_argument("fiction_url")
        parser.add_argument("--username", required=True)
        parser.add_argument("--max-chapters", type=int, default=2, help="Limit website downloads. Use 0 for metadata only.")
        source = parser.add_mutually_exclusive_group()
        source.add_argument("--rss", action="store_true", help="Import the title and recent release links from Royal Road RSS.")
        source.add_argument("--author-export", metavar="PATH", help="Import complete chapters from an authorized local JSON export.")

    def handle(self, *args, **options):
        from_rss = options["rss"]
        limit = options["max_chapters"]
        url = options["fiction_url"]
        if limit < 0:
            raise CommandError("--max-chapters must be zero or greater.")
        if len(url) > 500:
            raise CommandError("The fiction URL must have at most 500 characters.")

        users = get_user_model()
        try:
            user = users.objects.get(username=options["username"])
        except users.DoesNotExist as exc:
            raise CommandError("No account exists with that username.") from exc

        try:
            job = import_novel(url, user, limit, from_rss=from_rss, author_export=options["author_export"])
        except RoyalRoadError as exc:
            raise CommandError(str(exc)) from exc
        result = (
            f"RSS, {job.releases_imported} release links, 0 chapters downloaded"
            if from_rss else f"{job.chapters_scraped} chapters from {job.get_source_display()}"
        )
        self.stdout.write(self.style.SUCCESS(f"Imported {job.novel.title} ({result}, job #{job.pk})."))
