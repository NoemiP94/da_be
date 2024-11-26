from django.urls import path

from goal.views import goals_by_dlc_view, goals_by_game_view, goal_list_view

urlpatterns = [
    path('goal/<int:game_id>/', goals_by_game_view, name='goals_by_game'),
    path('goal/<int:game_id>/dlc/<int:dlc_id>/', goals_by_dlc_view, name='goals_by_dlc'),
    path('all/', goal_list_view, name='goal_list')
]