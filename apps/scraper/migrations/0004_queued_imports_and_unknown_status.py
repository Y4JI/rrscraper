from django.db import migrations, models


def reset_unverified_status(apps, schema_editor):
    Novel = apps.get_model("scraper", "Novel")
    Job = apps.get_model("scraper", "Job")
    verified = Job.objects.filter(source="WEB", status="COMPLETED", novel_id__isnull=False).values("novel_id")
    rss_only = Job.objects.filter(source="RSS", status="COMPLETED", novel_id__isnull=False).exclude(novel_id__in=verified).values("novel_id")
    Novel.objects.filter(pk__in=rss_only, status="ONGOING", author_name="").update(status="UNKNOWN")


class Migration(migrations.Migration):
    dependencies = [("scraper", "0003_release_metadata_and_job_source")]
    operations = [
        migrations.AddField(model_name="job", name="active_key", field=models.CharField(max_length=50, null=True, blank=True, unique=True)),
        migrations.AlterField(model_name="novel", name="status", field=models.CharField(max_length=30, default="UNKNOWN", choices=[("UNKNOWN", "Unknown"), ("ONGOING", "Ongoing"), ("COMPLETED", "Completed"), ("HIATUS", "Hiatus"), ("STUB", "Stub")])),
        migrations.RunPython(reset_unverified_status, migrations.RunPython.noop),
    ]
