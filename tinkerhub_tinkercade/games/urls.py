from django.urls import path
from tinkerhub_tinkercade.games.views import (
    gamees_list_view,
    single_game_view,
    user_list_view,
    user_rank_view,
    game_list,
    game_detail,

)

app_name = "games"

urlpatterns = [
    path("all/<str:level>", view=gamees_list_view, name="games_list"),
    path("get-user-list/", view=user_list_view, name="user-list"),
    path("get/<slug:slug>/", view=single_game_view, name="single-game"),
    path('leaderboard/', view=user_rank_view, name='user-rank'),
    path('', game_list, name='game_list'),
    path('game/<slug:slug>/', game_detail, name='game_detail'),

    
]