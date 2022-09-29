from rest_framework import serializers

from testapi.models import TestModel1


class TestModel1Serializer(serializers.ModelSerializer):

    class Meta:
        model = TestModel1
        fields = '__all__'

