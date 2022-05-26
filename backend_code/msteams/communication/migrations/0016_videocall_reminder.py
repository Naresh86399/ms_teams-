
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0015_rename_team_videocallmailbox_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocall',
            name='reminder',
            field=models.BooleanField(default=False),
        ),
    ]
