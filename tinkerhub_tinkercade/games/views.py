from django.shortcuts import render, get_object_or_404
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
from tinkerhub_tinkercade.users.api.serializers import (
    UserSerializer
)
from tinkerhub_tinkercade.games.models import Games
from tinkerhub_tinkercade.users.models import User
from django.views.generic import TemplateView



# Create your views here.
class GamesListView(ListAPIView):
    serializer_class = GamesSerializer
    queryset = Games.objects.all()

    def get_queryset(self):
        level = self.kwargs.get('level')
        queryset = Games.objects.filter(level=level)
        return queryset

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

class UsersListView(ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        queryset = User.objects.order_by("points")
        return queryset
user_list_view = UsersListView.as_view()

 # Assuming you have a User model

class UserRankView(TemplateView):
    template_name = 'user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.order_by('-points')  # Retrieve users sorted by points
        context['users'] = users
        return context
user_rank_view = UserRankView.as_view()

def user_list(request):
    users=User.objects.order_by("-points")
    return render(request, 'user_list.html', {'users': users})

def game_list(request):
    games = Games.objects.order_by("level")
    resp = render(request, 'game_list.html', {'games': games})
    resp["ngrok-skip-browser-warning"]=False
    return resp

def game_detail(request, slug):
    game = Games.objects.get(slug=slug)
    return render(request, 'game_detail.html', {'game': game})