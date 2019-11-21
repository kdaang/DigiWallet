from django.conf import settings
from django.db import models
from v1.cards.models import Card
from v1.users.models import User, UserTypes


class CustomerManager(models.Manager):
    def create_customer(self, **fields):
        merchant = self.model(**fields)
        merchant.save(using=self._db)

        return merchant

    def signup(self, **fields):
        user_data = fields.pop('user')
        user_data['user_type'] = UserTypes.CUSTOMER
        card = Card.objects.create_card(is_enabled=True)
        user = User.objects.create_user(**user_data)
        customer = self.create_customer(user=user, card=card, **fields)
        customer.save(using=self._db)

        return customer


class Customer(models.Model):
    objects = CustomerManager()

    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=False, on_delete=models.CASCADE)
    customer_id = models.BigAutoField(primary_key=True, unique=True)
    card = models.OneToOneField(to=Card, primary_key=False, on_delete=models.PROTECT)
    # TODO: CUSTOMER DETAILS
