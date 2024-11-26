from django.urls import path

from games.views import game_detail_view, game_list_view


urlpatterns = [ 
    path('games/', game_list_view, name='games_list'), 
    
    path('detail/<int:game_id>/', game_detail_view, name='game_detail')
]