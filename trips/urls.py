from rest_framework.routers import DefaultRouter

from trips.views import TripViewSet, TripVisitViewSet

router = DefaultRouter()
router.register('visit', TripVisitViewSet, basename='TripVisit')
router.register('', TripViewSet, basename='Trip')
urlpatterns = router.urls
