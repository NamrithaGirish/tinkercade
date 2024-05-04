# from __future__ import annotations

from typing import Any

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from django.http import HttpRequest
from allauth.socialaccount.models import SocialLogin
# if typing.TYPE_CHECKING:
#     from allauth.socialaccount.models import SocialLogin
#     from django.http import HttpRequest

#     from tinkerhub_tinkercade.users.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest) -> bool:
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(
        self,
        request: HttpRequest,
        sociallogin: SocialLogin,):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)

    def pre_social_login(self, request, sociallogin):
        if sociallogin.is_existing:
            return
        if "email" not in sociallogin.account.extra_data:
            return
        try:
            user = User.objects.get(email=sociallogin.account.extra_data["email"])
            sociallogin.connect(request, user)
        except User.DoesNotExist:
            pass
