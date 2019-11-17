from django.db import models
from DigiWallet.settings import AUTH_USER_MODEL
from v1.cards.models import Card


class CustomerManager(models.Manager):
    def create_customer(self, **fields):
        pass


class Customer(models.Model):
    objects = CustomerManager()

    user = models.OneToOneField(to=AUTH_USER_MODEL, primary_key=False, on_delete=models.CASCADE)
    customer_id = models.BigAutoField(primary_key=True, unique=True)
    card = models.OneToOneField(to=Card, primary_key=False, on_delete=models.PROTECT)
    # TODO: CUSTOMER DETAILS
