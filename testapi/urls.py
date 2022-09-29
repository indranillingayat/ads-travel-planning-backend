from rest_framework.routers import DefaultRouter

from testapi.views import TestModel1ViewSet

router = DefaultRouter()

router.register('test-api1', TestModel1ViewSet)

urlpatterns = router.urls
