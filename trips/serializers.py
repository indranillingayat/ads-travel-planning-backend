from django.contrib.auth import get_user_model
from rest_framework import serializers

from trips.models import Trip, TripVisit
from users.serializers import UserMinInfoSerializer

User = get_user_model()


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
    ads_participants = UserMinInfoSerializer(many=True, read_only=True)
    external_participants = UserMinInfoSerializer(many=True, read_only=True)

    class Meta:
        model = TripVisit
        fields = ('id', 'note', 'visit_date', 'share_with_ads', 'share_externally', 'visit_account', 'start_time',
                  'end_time', 'ads_participants', 'external_participants')
        read_only_fields = ('id',)


class TripWithVisitsSerializer(serializers.ModelSerializer):
    owner = UserMinInfoSerializer(read_only=True)
    tripvisit_set = EmbeddedTripVisitSerializer(many=True)

    def create(self, validated_data):
        trip_visits = self.initial_data.pop('tripvisit_set')
        validated_data.pop('tripvisit_set')
        trip = Trip.objects.create(**validated_data)
        try:
            for visit in trip_visits:
                ads_participants = User.objects.filter(id__in=visit.pop('ads_participants', []), user_type=1)
                external_participants = User.objects.filter(id__in=visit.pop('external_participants', []), user_type=2)
                serializer = EmbeddedTripVisitSerializer(data=visit)
                serializer.is_valid(raise_exception=True)
                new_visit = serializer.save(trip=trip)
                new_visit.ads_participants.set(ads_participants)
                new_visit.external_participants.set(external_participants)

        except Exception:
            trip.delete()
            raise

        return trip

    class Meta:
        model = Trip
        fields = ('id', 'trip_name', 'comments', 'start_date', 'end_date', 'owner', 'tripvisit_set')
        read_only_fields = ('id', 'owner')
