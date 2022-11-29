from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from trips.models import Trip, TripVisit
from trips.permissions import TripPermission
from trips.serializers import TripSerializer, TripVisitSerializer, TripWithVisitsSerializer, TripVisitListSerializer
from utils.views.viewset import AppViewProvider


class TripViewSet(AppViewProvider, ModelViewSet):
    permission_classes = [IsAuthenticated, TripPermission, ]
    serializer_class = TripWithVisitsSerializer
    queryset = Trip.objects.none()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TripVisitViewSet(AppViewProvider, ModelViewSet):
    serializer_class = TripVisitSerializer
    queryset = TripVisit.objects.all()
    filter_fields = ('trip', 'visit_account')

    @action(methods=["get"], detail=False)
    def list_trip_visits(self, request):
        return self.custom_list(TripVisitListSerializer, TripVisit.objects.filter(trip__owner=request.user))
