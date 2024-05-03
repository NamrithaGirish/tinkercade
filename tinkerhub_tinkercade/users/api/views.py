from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user_model

from .serializers import UserSerializer

User = get_user_model()

class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                data = SocialAccount.objects.get(
                    provider="google", user=user
                ).extra_data
                picture = data.get("picture")
                user.profile_image = picture
                if not user.name:
                    user.name = user.username
                user.save()

            except SocialAccount.DoesNotExist:
                pass
            except KeyError:
                pass
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

