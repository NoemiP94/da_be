# Generated by Django 5.0.7 on 2024-11-12 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('charcClass', models.CharField(max_length=200)),
                ('specialisation', models.CharField(max_length=200)),
                ('where', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('affiliation', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('race', models.CharField(max_length=200)),
                ('romanceable', models.BooleanField()),
                ('image', models.ImageField(upload_to='')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='games.videogame')),
            ],
        ),
    ]
