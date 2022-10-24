from rest_framework.serializers import ModelSerializer

from accounts.models import Account


class AccountMinSerializer(ModelSerializer):

    class Meta:
        fields = ('account_guid', 'account_name')
        models = Account
