from django.shortcuts import render
from django.http import Http404, JsonResponse
from .models import Goal

# Create your views here.

def goal_list_view(request):
    try:
        goals = Goal.objects.all()
        goal_list = list(goals.values('id', 'name', 'requirements', 'points', 'award_type', 'game_id','dlc_id', 'image_base64'))
        return JsonResponse(goal_list, safe=False)
    except Goal.DoesNotExist:
        raise Http404("Goal does not exist")
    
def goals_by_game_view(request, game_id):
    try:
        goals = Goal.objects.filter(game_id=game_id, dlc_id__isnull=True)
        goal_list = [
            {
                'id': goal.id, 
                'name': goal.name, 
                'requirements': goal.requirements, 
                'points': goal.points, 
                'award_type': goal.award_type, 
                'game_id': goal.game_id, 
                'dlc_id': goal.dlc,
                'image_base64': goal.image_base64
            }
            for goal in goals
            ]
        return JsonResponse(goal_list, safe=False)
    except Goal.DoesNotExist:
        raise Http404("Goal does not exist")
    

def goals_by_dlc_view(request, game_id, dlc_id):
        try:
            goals = Goal.objects.filter(game_id=game_id, dlc_id=dlc_id)
            goal_list = [
                {
                    'id': goal.id, 
                    'name': goal.name, 
                    'requirements': goal.requirements, 
                    'points': goal.points, 
                    'award_type': goal.award_type, 
                    'game_id': goal.game_id, 
                    'dlc_id': goal.dlc_id,
                    'image_base64': goal.image_base64
                }
                for goal in goals
                ]
            return JsonResponse(goal_list, safe=False)
        except Goal.DoesNotExist:
            raise Http404("Goal does not exist")
