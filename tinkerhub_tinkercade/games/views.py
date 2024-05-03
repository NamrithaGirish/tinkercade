from django.shortcuts import render
from rest_framework.generics import (
    # CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    # UpdateAPIView,
    # ListCreateAPIView,
    # get_object_or_404,
)

from tinkerhub_tinkercade.games.serializers import (
    GamesSerializer
)
from tinkerhub_tinkercade.games.models import Games

# Create your views here.
class GamesListView(ListAPIView):
    serializer_class = GamesSerializer
    queryset = Games.objects.all()
    ordering = ["level"]

    class Meta:
        model = Games
        fields = "__all__"

gamees_list_view = GamesListView.as_view()

class SingleGameView(RetrieveAPIView):
    queryset = Games.objects.all()
    lookup_field = "slug"
    serializer_class = GamesSerializer

    class Meta:
        model = Games
        fields = "__all__"

single_game_view = SingleGameView.as_view()