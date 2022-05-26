
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0009_p2pvideocall'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='img',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='message',
            name='type',
            field=models.CharField(default='txt', max_length=20),
            preserve_default=False,
        ),
    ]
