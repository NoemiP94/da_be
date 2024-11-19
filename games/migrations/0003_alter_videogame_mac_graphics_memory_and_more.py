# Generated by Django 5.0.7 on 2024-11-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_videogame_engine_videogame_game_mode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='mac_graphics_memory',
            field=models.TextField(default='mac_graphics_memory'),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='mac_hard_drive',
            field=models.TextField(default='mac_hard_drive'),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='mac_system_RAM',
            field=models.TextField(default='mac_system_RAM'),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='pc_graphics_memory',
            field=models.TextField(default='pc_graphics_memory'),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='pc_hard_drive',
            field=models.TextField(default='pc_hard_drive'),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='pc_system_RAM',
            field=models.TextField(default='pc_system_RAM'),
        ),
    ]