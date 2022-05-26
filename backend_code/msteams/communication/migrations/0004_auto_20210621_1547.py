
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0003_videocall_meeting_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocall',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='videocall',
            name='token',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videocallparticipant',
            name='in_call',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
