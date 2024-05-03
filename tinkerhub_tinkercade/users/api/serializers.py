from rest_framework import serializers

from tinkerhub_tinkercade.users.models import User


class UserSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ["username"]

        # extra_kwargs = {
        #     "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        # }
