from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination


class AppViewProvider:
    """
    Class which can be inherited in other viewsets which will provide list of common settings to views
    """
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    authentication_classes = (TokenAuthentication,)
