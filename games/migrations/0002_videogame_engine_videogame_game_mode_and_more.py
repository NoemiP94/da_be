# Generated by Django 5.0.7 on 2024-11-19 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogame',
            name='engine',
            field=models.CharField(default='engine', max_length=300),
        ),
        migrations.AddField(
            model_name='videogame',
            name='game_mode',
            field=models.CharField(default='game_mode', max_length=300),
        ),
        migrations.AddField(
            model_name='videogame',
            name='gameplay',
            field=models.TextField(default='gameplay'),
        ),
        migrations.AddField(
            model_name='videogame',
            name='image',
            field=models.ImageField(default='images/default_image.jpg', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videogame',
            name='mac_graphics_card',
            field=models.TextField(default='mac_graphics_card'),
        ),
        migrations.AddField(
            model_name='videogame',
            name='mac_graphics_memory',
            field=models.CharField(default='mac_graphics_memory', max_length=500),
        ),
        migrations.AddField(
            model_name='videogame',
            name='mac_hard_drive',
            field=models.CharField(default='mac_hard_drive', max_length=500),
        ),
        migrations.AddField(
            model_name='videogame',
            name='mac_other',
            field=models.TextField(default='mac_other'),
        ),
        migrations.AddField(
            model_name='videogame',
            name='mac_system_CPU',
            field=models.TextField(default='mac_system_CPU'),
        ),
        migrations.AddField(
            model_name='videogame',
            name='mac_system_OS',
            field=models.TextField(default='mac_system_OS'),
        ),
        migrations.AddField(
            model_name='videogame',
            name='mac_system_RAM',
            field=models.CharField(default='mac_system_RAM', max_length=500),
        ),
        migrations.AddField(
            model_name='videogame',
            name='pc_graphics_card',
            field=models.TextField(default='pc_graphics_card'),
        ),
        migrations.AddField(
            model_name='videogame',
            name='pc_graphics_memory',
            field=models.CharField(default='pc_graphics_memory', max_length=500),
        ),
        migrations.AddField(
            model_name='videogame',
            name='pc_hard_drive',
            field=models.CharField(default='pc_hard_drive', max_length=500),
        ),
        migrations.AddField(
            model_name='videogame',
            name='pc_other',
            field=models.TextField(default='pc_other'),
        ),
        migrations.AddField(
            model_name='videogame',
            name='pc_system_CPU',
            field=models.TextField(default='pc_system_CPU'),
        ),
        migrations.AddField(
            model_name='videogame',
            name='pc_system_OS',
            field=models.TextField(default='pc_system_OS'),
        ),
        migrations.AddField(
            model_name='videogame',
            name='pc_system_RAM',
            field=models.CharField(default='pc_system_RAM', max_length=500),
        ),
        migrations.AddField(
            model_name='videogame',
            name='storyline',
            field=models.TextField(default='storyline'),
        ),
    ]
