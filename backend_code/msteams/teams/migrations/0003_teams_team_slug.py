
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_teams_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='team_slug',
            field=models.CharField(default='team-slug', max_length=100),
            preserve_default=False,
        ),
    ]
