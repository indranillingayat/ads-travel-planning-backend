import uuid

from django.db import models


class Account(models.Model):
    account_guid = models.CharField(max_length=255, primary_key=True)
    account_owner = models.CharField(max_length=255)
    department_name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=255)
    supplier_tier = models.CharField(max_length=255)
    customer_agent = models.CharField(max_length=255)
    sales_3y = models.DecimalField(max_digits=15, decimal_places=2)
    sales_cy = models.DecimalField(max_digits=15, decimal_places=2)
    margin_3y = models.DecimalField(max_digits=15, decimal_places=2)
    margin_cy = models.DecimalField(max_digits=15, decimal_places=2)
    open_quotes = models.DecimalField(max_digits=15, decimal_places=2)
    last_activity = models.CharField(max_length=255)
    address = models.CharField(max_length=4000)
    as_of_date = models.DateField(auto_now_add=True)
