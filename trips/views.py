from rest_framework.viewsets import ModelViewSet

from trips.models import Trip
from trips.serializers import TripSerializer
from utils.views.viewset import AppViewProvider


class TripViewSet(AppViewProvider, ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save(owner=self.request.user)  # type: Trip
