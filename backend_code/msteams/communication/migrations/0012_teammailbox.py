
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_teamtodo'),
        ('communication', '0011_alter_message_msg_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMailBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('messsage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communication.message')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.teams')),
            ],
        ),
    ]
