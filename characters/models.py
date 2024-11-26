import base64
from django.db import models
from games.models import VideoGame

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=200)
    charcClass= models.CharField(max_length=200)
    specialisation=models.CharField(max_length=200)
    where=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    affiliation=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    race=models.CharField(max_length=200)
    romanceable=models.BooleanField()
    image_base64= models.TextField()
    game = models.ForeignKey(VideoGame, on_delete=models.CASCADE, related_name='characters')
    description = models.TextField()

    def __str__(self): return self.name

    # convert img in base64 e salva la stringa nel campo
    def save_image_as_base64(self, image_file):
        self.image_base64 = base64.b64encode(image_file.read()).decode()

    # ritorna l'img come stringa base 64
    def get_image_as_base64(self):
        return self.image_base64