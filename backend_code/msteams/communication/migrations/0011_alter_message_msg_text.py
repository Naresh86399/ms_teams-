
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0010_auto_20210701_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg_text',
            field=models.TextField(null=True),
        ),
    ]
