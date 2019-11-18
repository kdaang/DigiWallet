from django.db import models
from django.conf import settings


class Transaction(models.Model):
    transaction_id = models.BigAutoField(primary_key=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    from_user = models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=False, on_delete=models.PROTECT,
                                     related_name='from_user')
    to_user = models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=False, on_delete=models.PROTECT,
                                   related_name='to_user')
    total = models.BigIntegerField()
