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

    def __str__(self):
        return self.trip_name


class TripVisit(UUIDPKAbstractModel):
    note = models.TextField()
    visit_date = models.DateField()
    share_with_ads = models.BooleanField(default=False)
    share_externally = models.BooleanField(default=False)
    ads_participants = models.ManyToManyField(User, related_name='ads_visits', blank=True)
    external_participants = models.ManyToManyField(User, related_name='external_visits', blank=True)
    account_snapshot = models.JSONField(null=True, blank=True)
    visit_account = models.ForeignKey('accounts.Account', null=True, on_delete=models.SET_NULL)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.trip} - {self.note}"
