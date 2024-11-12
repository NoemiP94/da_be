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
    image= models.ImageField()
    game = models.ForeignKey(VideoGame, on_delete=models.CASCADE, related_name='characters')

    def __str__(self): return self.name
