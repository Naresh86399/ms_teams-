
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communication', '0008_auto_20210623_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='P2PVideocall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_slug', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('started_at', models.BigIntegerField()),
                ('is_completed', models.BooleanField(default=False)),
                ('s_id', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_c', to=settings.AUTH_USER_MODEL)),
                ('user_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_d', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
