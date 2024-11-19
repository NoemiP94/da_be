from django.http import Http404, JsonResponse
from .models import VideoGame

# Create your views here.

def game_list_view(request):
    games = VideoGame.objects.all()
    game_list= list(games.values('id', 'title', 'year'))
    return JsonResponse(game_list, safe=False) 

def game_detail_view(request, game_id):
    try:
        game = VideoGame.objects.get(id=game_id)
        game_data = {
            'id' : game.id,
            'title': game.title,
            'year': game.year,
            'storyline' : game.storyline,
            'gameplay': game.gameplay,
            'engine': game.engine,
            'game_mode': game.game_mode,
            'pc_system_OS': game.pc_system_OS,
            'pc_system_CPU': game.pc_system_CPU,
            'pc_system_RAM': game.pc_system_RAM,
            'pc_graphics_card': game.pc_graphics_card,
            'pc_graphics_memory': game.pc_graphics_memory,
            'pc_hard_drive': game.pc_hard_drive,
            'pc_other': game.pc_other,
            'mac_system_OS': game.mac_system_OS,
            'mac_system_CPU': game.mac_system_CPU,
            'mac_system_RAM': game.mac_system_RAM,
            'mac_graphics_card': game.mac_graphics_card,
            'mac_graphics_memory': game.mac_graphics_memory,
            'mac_hard_drive': game.mac_hard_drive,
            'mac_other': game.mac_other,
            'image_url':request.build_absolute_uri(game.image.url) if game.image else None    
        }
        return JsonResponse(game_data)
    except VideoGame.DoesNotExist:
        raise Http404("VideoGame does not exist")
