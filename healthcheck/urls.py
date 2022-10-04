from django.urls import path

from healthcheck.views import health_check

urlpatterns = [
    path('', health_check)
]
