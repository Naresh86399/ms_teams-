
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communication', '0007_auto_20210623_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatUUID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_id', models.UUIDField(default=uuid.uuid4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_a', to=settings.AUTH_USER_MODEL)),
                ('user_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_b', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='usermailbox',
            name='thread_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communication.chatuuid'),
        ),
    ]
