
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0014_videocallmailbox'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videocallmailbox',
            old_name='team',
            new_name='video',
        ),
    ]
