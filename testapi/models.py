from django.db import models


class TestModel1(models.Model):
    name = models.CharField(max_length=255, null=True)
    age = models.PositiveIntegerField()
