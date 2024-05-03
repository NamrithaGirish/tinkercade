from rest_framework.serializers import (
    ModelSerializer,
    # SerializerMethodField,
    # Serializer,
    # EmailField,
    # FileField,
    # ChoiceField,
)
from tinkerhub_tinkercade.games.models import (
    Games
)

class GamesSerializer(ModelSerializer):
    class Meta:
        model = Games
        fields = "__all__"