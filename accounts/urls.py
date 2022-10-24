from rest_framework.routers import DefaultRouter

from accounts.views import AccountMinViewSet

router = DefaultRouter()
router.register('account-basic', AccountMinViewSet, basename='AccountBasic')
urlpatterns = router.urls
