from django.db import models
from v1.customers.models import Customer
from v1.merchants.models import Merchant


class CompanyCustomer(models.Model):
    company = models.OneToOneField(to=Merchant, primary_key=False, on_delete=models.CASCADE)
    customer = models.OneToOneField(to=Customer, primary_key=False, on_delete=models.CASCADE)
    points = models.BigIntegerField()
