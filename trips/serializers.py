from rest_framework import serializers

from trips.models import Trip, TripVisit
from users.serializers import UserMinInfoSerializer


class TripSerializer(serializers.ModelSerializer):
    owner = UserMinInfoSerializer(read_only=True)

    class Meta:
        model = Trip
        fields = '__all__'


class TripVisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = TripVisit
        fields = '__all__'
