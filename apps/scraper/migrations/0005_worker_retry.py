from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("scraper", "0004_queued_imports_and_unknown_status")]
    operations = [
        migrations.AddField(model_name="job", name="attempts", field=models.PositiveIntegerField(default=0)),
        migrations.AddField(model_name="job", name="retry_at", field=models.DateTimeField(null=True, blank=True)),
        migrations.CreateModel(name="WorkerHeartbeat", fields=[
            ("name", models.CharField(max_length=30, primary_key=True, serialize=False)),
            ("last_seen", models.DateTimeField()),
        ]),
    ]
