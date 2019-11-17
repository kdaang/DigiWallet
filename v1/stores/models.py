from django.db import models
from v1.merchants.models import Merchant


class Store(models.Model):
    company = models.OneToOneField(to=Merchant, primary_key=False, on_delete=models.CASCADE)
    store_id = models.BigAutoField(primary_key=True, unique=True)
    # TODO: ADD EMPLOYEES ONETOONEFIELD

