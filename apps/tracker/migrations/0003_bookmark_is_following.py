from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("tracker", "0002_bookmark_last_read_release")]
    operations = [migrations.AddField(model_name="bookmark", name="is_following", field=models.BooleanField(default=True))]
