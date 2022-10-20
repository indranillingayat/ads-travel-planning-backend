from django.contrib.auth import get_user_model
from django.db import models

from utils.base_model import UUIDPKAbstractModel


User = get_user_model()


class Trip(UUIDPKAbstractModel):
    trip_name = models.CharField(max_length=255)
    comments = models.TextField(null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class TripVisit(UUIDPKAbstractModel):
    note = models.TextField()
    trip_date = models.DateField()

