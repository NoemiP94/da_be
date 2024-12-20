# Generated by Django 5.0.7 on 2024-11-25 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0003_alter_videogame_mac_graphics_memory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('requirements', models.TextField()),
                ('points', models.CharField(max_length=100)),
                ('award_type', models.CharField(max_length=300)),
                ('image_base64', models.TextField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal', to='games.videogame')),
            ],
        ),
    ]
