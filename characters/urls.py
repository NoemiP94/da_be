from django.urls import path
from .views import characters_by_game_view

urlpatterns = [
    path('game/<int:game_id>/', characters_by_game_view, name='characters_by_game')
]
