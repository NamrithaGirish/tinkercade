from django.urls import path
from tinkerhub_tinkercade.games.views import (
    gamees_list_view,
    single_game_view,

)

app_name = "games"

urlpatterns = [
    path("all/", view=gamees_list_view, name="games_list"),
    path("get/<slug:slug>/", view=single_game_view, name="single-game"),

]