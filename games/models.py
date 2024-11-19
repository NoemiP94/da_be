from django.db import models

# Create your models here.
class VideoGame(models.Model):
    title= models.CharField(max_length=300)
    year= models.IntegerField()
    storyline = models.TextField(default='storyline')
    gameplay = models.TextField(default='gameplay')
    image = models.ImageField()
    engine = models.CharField(max_length=300, default='engine')
    game_mode = models.CharField(max_length=300, default='game_mode')
    # requisiti sistema
    pc_system_OS = models.TextField(default='pc_system_OS')
    pc_system_CPU = models.TextField(default='pc_system_CPU')
    pc_system_RAM = models.CharField(max_length=500, default='pc_system_RAM')
    pc_graphics_card = models.TextField(default='pc_graphics_card')
    pc_graphics_memory = models.CharField(max_length=500, default='pc_graphics_memory')
    pc_hard_drive = models.CharField(max_length=500, default='pc_hard_drive')
    pc_other = models.TextField(default='pc_other')

    mac_system_OS = models.TextField(default='mac_system_OS')
    mac_system_CPU = models.TextField(default='mac_system_CPU')
    mac_system_RAM = models.CharField(max_length=500, default='mac_system_RAM')
    mac_graphics_card = models.TextField(default='mac_graphics_card')
    mac_graphics_memory = models.CharField(max_length=500, default='mac_graphics_memory')
    mac_hard_drive = models.CharField(max_length=500, default='mac_hard_drive')
    mac_other = models.TextField(default='mac_other')
    def __str__(self): return self.title