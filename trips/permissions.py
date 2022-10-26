from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission, SAFE_METHODS

from users.permissions import CPermission

User = get_user_model()


class TripPermission(BasePermission):

    @staticmethod
    def _has_create_trip_permission(user: User):
        return user.has_perm(CPermission.get_create_trip_permission())

    def has_object_permission(self, request, view, obj):
        action = view.action

        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user

    def has_permission(self, request, view):
        action = view.action
        if action == 'create':
            return self._has_create_trip_permission(request.user)

        return True
