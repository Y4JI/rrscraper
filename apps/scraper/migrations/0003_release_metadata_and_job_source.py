import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("scraper", "0002_unique_novel_source_chapter")]

    operations = [
        migrations.AddField(
            model_name="job",
            name="source",
            field=models.CharField(
                choices=[
                    ("LEGACY", "Earlier import"),
                    ("RSS", "Royal Road RSS"),
                    ("WEB", "Royal Road website"),
                    ("AUTHOR", "Author-provided export"),
                ],
                default="LEGACY",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="job",
            name="releases_imported",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name="ChapterRelease",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("royalroad_chapter_id", models.CharField(max_length=50)),
                ("title", models.CharField(max_length=255)),
                ("source_url", models.URLField(max_length=500)),
                ("release_date", models.DateTimeField(blank=True, null=True)),
                ("novel", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="releases", to="scraper.novel")),
            ],
            options={
                "ordering": [models.F("release_date").desc(nulls_last=True), "-pk"],
                "constraints": [models.UniqueConstraint(fields=("novel", "royalroad_chapter_id"), name="unique_novel_release")],
            },
        ),
    ]
