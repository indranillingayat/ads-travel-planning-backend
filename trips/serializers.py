from rest_framework import serializers

from trips.models import Trip, TripVisit
from users.serializers import UserMinInfoSerializer


class TripSerializer(serializers.ModelSerializer):
    owner = UserMinInfoSerializer(read_only=True)

    class Meta:
        model = Trip
        fields = '__all__'
        read_only_fields = ('id', 'owner')


class TripVisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = TripVisit
        fields = '__all__'
        read_only_fields = ('id', 'account_snapshot')


class EmbeddedTripVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripVisit
        fields = ('id', 'note', 'visit_date', 'share_with_ads', 'share_externally', 'visit_account', 'start_time',
                  'end_time')
        read_only_fields = ('id',)


class TripWithVisitsSerializer(serializers.ModelSerializer):
    owner = UserMinInfoSerializer(read_only=True)
    tripvisit_set = EmbeddedTripVisitSerializer(many=True)

    def create(self, validated_data):
        trip_visits = validated_data.pop('tripvisit_set')
        trip = Trip.objects.create(**validated_data)
        for visit in trip_visits:
            TripVisit.objects.create(trip=trip, **visit)

        return trip

    class Meta:
        model = Trip
        fields = ('id', 'trip_name', 'comments', 'start_date', 'end_date', 'owner', 'tripvisit_set')
        read_only_fields = ('id', 'owner')
