from django.urls import path

from dlc.views import dlc_by_game_view


urlpatterns = [
    path('<int:game_id>/', dlc_by_game_view, name='dlc_by_game')
]