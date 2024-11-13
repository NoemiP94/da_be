from django.shortcuts import render
from .models import Character

# Create your views here.

def characters_by_game_view(request, game_id):
    characters = Character.objects.filter(game_id=game_id)
    return render(request, 'characters_by_game.html', {'characters': characters})