from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from trips.models import Trip, TripVisit
from trips.permissions import TripPermission
from trips.serializers import TripSerializer, TripVisitSerializer
from utils.views.viewset import AppViewProvider


class TripViewSet(AppViewProvider, ModelViewSet):
    permission_classes = [IsAuthenticated, TripPermission, ]
    serializer_class = TripSerializer
    queryset = Trip.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TripVisitViewSet(AppViewProvider, ModelViewSet):
    serializer_class = TripVisitSerializer
    queryset = TripVisit.objects.all()
    filter_fields = ('trip', 'visit_account')
