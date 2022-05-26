
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0005_alter_videocall_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videocall',
            old_name='token',
            new_name='s_id',
        ),
    ]
