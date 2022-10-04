from django.urls import path

from users.views import CustomObtainAuthToken

urlpatterns = [
    path('login/', CustomObtainAuthToken.as_view())
]

