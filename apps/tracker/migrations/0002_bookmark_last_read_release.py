from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("scraper", "0003_release_metadata_and_job_source"),
        ("tracker", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookmark",
            name="last_read_release",
            field=models.ForeignKey(
                "scraper.ChapterRelease",
                on_delete=django.db.models.deletion.SET_NULL,
                null=True,
                blank=True,
                related_name="bookmarks",
            ),
        ),
    ]
