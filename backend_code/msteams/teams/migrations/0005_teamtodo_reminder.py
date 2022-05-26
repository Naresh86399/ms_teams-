
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_teamtodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamtodo',
            name='reminder',
            field=models.BooleanField(default=False),
        ),
    ]
