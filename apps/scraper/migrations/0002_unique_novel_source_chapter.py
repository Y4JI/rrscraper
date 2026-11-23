from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("scraper", "0001_initial")]

    operations = [
        migrations.AddConstraint(
            model_name="chapter",
            constraint=models.UniqueConstraint(
                fields=["novel", "royalroad_chapter_id"], name="unique_novel_source_chapter"
            ),
        ),
    ]
