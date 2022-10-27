from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission, SAFE_METHODS

from users.permissions import CPermission

User = get_user_model()


class TripPermission(BasePermission):
    """
    This class will implement view based permissions, so returns True always for the views to which conditions do not
    apply
    """

    @staticmethod
    def _has_create_trip_permission(user: User):
        return user.has_perm(CPermission.get_create_trip_permission())

    def has_object_permission(self, request, view, instance):

        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return instance.owner == request.user

    def has_permission(self, request, view):
        action = view.action
        if action == 'create':
            return self._has_create_trip_permission(request.user)

        return True
