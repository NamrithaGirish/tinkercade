from rest_framework import permissions
from rest_framework.request import Request


class IsCoordinator(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        if request.user.is_authenticated:
            if request.user.user_type == "C":
                return True
