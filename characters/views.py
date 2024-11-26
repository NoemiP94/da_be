from django.http import Http404, JsonResponse
from .models import Character

# Create your views here.

def characters_by_game_view(request, game_id):
    characters = Character.objects.filter(game_id=game_id)
    characters_list = [ 
    { 
        'id': character.id,
        'name': character.name, 
        'class': character.charcClass,
        'specialisation': character.specialisation,
        'from': character.where,
        'title': character.title,
        'affiliation': character.affiliation,
        'gender': character.gender,
        'race': character.race,
        'romanceable': character.romanceable,
        'description': character.description,
        'game_id': character.game_id, 
        'image_base64': character.image_base64
        
        } 
        for character in characters 
        ]
    return JsonResponse(characters_list, safe=False)

def character_detail_view(request, character_id):
    try:
        character = Character.objects.get(id=character_id)
        character_data = {
            'id' : character.id,
            'name': character.name, 
            'class': character.charcClass,
            'specialisation': character.specialisation,
            'from': character.where,
            'title': character.title,
            'affiliation': character.affiliation,
            'gender': character.gender,
            'race': character.race,
            'romanceable': character.romanceable,
            'description': character.description,
            'game_id': character.game_id, 
            'image_base64': character.image_base64
        }
        return JsonResponse(character_data)
    except Character.DoesNotExist:
        raise Http404("Character does not exist")
    

def characters_list_view(request):
    characters  = Character.objects.all()
    character_list = list(characters.values('id' ,'name','game_id'))  
    return JsonResponse(character_list, safe=False)


