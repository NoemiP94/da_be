# Generated by Django 5.0.7 on 2024-11-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_character_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='image',
        ),
        migrations.AddField(
            model_name='character',
            name='image_base64',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
