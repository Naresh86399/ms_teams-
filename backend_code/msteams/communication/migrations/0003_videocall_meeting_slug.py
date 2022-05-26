
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0002_videocall_team_associated'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocall',
            name='meeting_slug',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
