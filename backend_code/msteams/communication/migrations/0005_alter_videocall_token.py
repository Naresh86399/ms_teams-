
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0004_auto_20210621_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocall',
            name='token',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]