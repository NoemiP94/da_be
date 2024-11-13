from django.http import JsonResponse
from .models import Character

# Create your views here.

def characters_by_game_view(request, game_id):
    characters = Character.objects.filter(game_id=game_id)
    characters_list = list(characters.values('name','charcClass', 'specialisation', 'where','title','affiliation','gender', 'race','romanceable', 'image' ,'game_id'))
    return JsonResponse(characters_list, safe=False)