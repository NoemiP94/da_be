from django.urls import path 
from .views import game_list_view 

urlpatterns = [ 
    path('games/', game_list_view, name='games_list'), 
]