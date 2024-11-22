from django.urls import path

from goal.views import goals_by_game_view, goal_list_view

urlpatterns = [
    path('goal/<int:game_id>/', goals_by_game_view, name='goals_by_game'),
    path('all/', goal_list_view, name='goal_list')
]