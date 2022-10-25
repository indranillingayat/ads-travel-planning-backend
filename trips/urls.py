from rest_framework.routers import DefaultRouter

from trips.views import TripViewSet

router = DefaultRouter()
router.register('', TripViewSet, basename='Trip')
urlpatterns = router.urls
