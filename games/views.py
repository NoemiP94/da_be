from django.http import JsonResponse
from .models import VideoGame

# Create your views here.

def game_list_view(request):
    games = VideoGame.objects.all()
    game_list= list(games.values('id', 'title', 'year'))
    return JsonResponse(game_list, safe=False) 


