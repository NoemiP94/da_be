from django.db import models
from dlc.models import Dlc
from games.models import VideoGame
import base64

# Create your models here.

class Goal(models.Model):
    name = models.CharField(max_length=300)
    requirements = models.TextField()
    points = models.CharField(max_length=100)
    award_type = models.CharField(max_length=300)
    game = models.ForeignKey(VideoGame, on_delete=models.CASCADE, related_name='goal',default='', null=True, blank=True)
    dlc = models.ForeignKey(Dlc, on_delete=models.CASCADE, related_name='goal',default='', null=True, blank=True)
    image_base64 = models.TextField()

    def __str__(self):return self.name

    # convert img in base64 e salva la stringa nel campo
    def save_image_as_base64(self, image_file):
        self.image_base64 = base64.b64encode(image_file.read()).decode()

    # ritorna l'img come stringa base 64
    def get_image_as_base64(self):
        return self.image_base64