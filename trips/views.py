from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from trips.models import Trip
from trips.permissions import TripPermission
from trips.serializers import TripSerializer
from utils.views.viewset import AppViewProvider


class TripViewSet(AppViewProvider, ModelViewSet):
    permission_classes = [IsAuthenticated, TripPermission, ]
    serializer_class = TripSerializer
    queryset = Trip.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save(owner=self.request.user)  # type: Trip
