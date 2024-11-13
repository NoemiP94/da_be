from django.http import JsonResponse
from .models import Character

# Create your views here.

def characters_by_game_view(request, game_id):
    characters = Character.objects.filter(game_id=game_id)
    characters_list = [ 
    { 
        'name': character.name, 
        'class': character.charcClass,
        'specialisation': character.specialisation,
        'from': character.where,
        'title': character.title,
        'affiliation': character.affiliation,
        'gender': character.gender,
        'race': character.race,
        'romanceable': character.romanceable,
        'game_id': character.game_id, 
        'image_url': request.build_absolute_uri(character.image.url) if character.image else None 

        } 
        for character in characters 
        ]
    return JsonResponse(characters_list, safe=False)

