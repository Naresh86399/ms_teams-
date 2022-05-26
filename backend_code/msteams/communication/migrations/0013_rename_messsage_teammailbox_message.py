
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0012_teammailbox'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammailbox',
            old_name='messsage',
            new_name='message',
        ),
    ]
