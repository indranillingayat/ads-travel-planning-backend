from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import CustomObtainAuthToken, UserViewSet

urlpatterns = [
    path('login/', CustomObtainAuthToken.as_view())
]

router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns.extend(router.urls)
