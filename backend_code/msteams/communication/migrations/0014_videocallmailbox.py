
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0013_rename_messsage_teammailbox_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoCallMailBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communication.message')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communication.videocall')),
            ],
        ),
    ]
