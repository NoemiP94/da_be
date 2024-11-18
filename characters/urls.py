from django.urls import path
from .views import character_detail_view, characters_by_game_view, characters_list_view

urlpatterns = [
    path('game/<int:game_id>/', characters_by_game_view, name='characters_by_game'),
    path('all/<int:character_id>/', character_detail_view, name='character_detail'),
    path('all/', characters_list_view, name='character_list')
]
