from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class AppViewProvider:
    """
    Class which can be inherited in other viewsets which will provide list of common settings to views
    """
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    pagination_class = LimitOffsetPagination
    authentication_classes = (TokenAuthentication,)

    def custom_list(self, serializer_klass, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = serializer_klass(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializer_klass(queryset, many=True)
        return Response(serializer.data)
