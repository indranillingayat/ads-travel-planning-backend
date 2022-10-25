from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserMinInfoSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, instance):
        return f"{instance.first_name} {instance.last_name}"

    class Meta:
        model = User
        fields = ('id', 'full_name')
