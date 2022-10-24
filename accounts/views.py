from rest_framework.viewsets import ModelViewSet

from accounts.models import Account
from accounts.serializers import AccountMinSerializer
from utils.views.viewset import AppViewProvider


class AccountMinViewSet(AppViewProvider, ModelViewSet):
    search_fields = ('account_name', )
    serializer_class = AccountMinSerializer

    def get_queryset(self):
        return Account.objects.all()
