from django.http import Http404, JsonResponse
from django.shortcuts import render

from dlc.models import Dlc

# Create your views here.

def dlc_by_game_view(request, game_id):
    try:
        dlcs = Dlc.objects.filter(game_id=game_id)
        dlc_list = [
            {
                'id': dlc.id,
                'title': dlc.title,
                'year':dlc.year,
                'content':dlc.content,
                'game_id': dlc.game_id,
                'image_base64': dlc.image_base64
            }
            for dlc in dlcs
            ]
        return JsonResponse(dlc_list, safe=False)
    except Dlc.DoesNotExist:
        raise Http404("Dlv does not exist")
