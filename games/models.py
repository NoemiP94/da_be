import base64
from django.db import models

# Create your models here.
class VideoGame(models.Model):
    title= models.CharField(max_length=300)
    year= models.IntegerField()
    storyline = models.TextField(default='storyline')
    gameplay = models.TextField(default='gameplay')
    image_base64 = models.TextField()
    engine = models.CharField(max_length=300, default='engine')
    game_mode = models.CharField(max_length=300, default='game_mode')
    # requisiti sistema
    pc_system_OS = models.TextField(default='pc_system_OS')
    pc_system_CPU = models.TextField(default='pc_system_CPU')
    pc_system_RAM = models.TextField(default='pc_system_RAM')
    pc_graphics_card = models.TextField(default='pc_graphics_card')
    pc_graphics_memory = models.TextField(default='pc_graphics_memory')
    pc_hard_drive = models.TextField(default='pc_hard_drive')
    pc_other = models.TextField(default='pc_other')

    mac_system_OS = models.TextField(default='mac_system_OS')
    mac_system_CPU = models.TextField(default='mac_system_CPU')
    mac_system_RAM = models.TextField(default='mac_system_RAM')
    mac_graphics_card = models.TextField(default='mac_graphics_card')
    mac_graphics_memory = models.TextField(default='mac_graphics_memory')
    mac_hard_drive = models.TextField(default='mac_hard_drive')
    mac_other = models.TextField(default='mac_other')
    def __str__(self): return self.title

    # convert img in base64 e salva la stringa nel campo
    def save_image_as_base64(self, image_file):
        self.image_base64 = base64.b64encode(image_file.read()).decode()

    # ritorna l'img come stringa base 64
    def get_image_as_base64(self):
        return self.image_base64