from DigiWallet.settings import AUTH_USER_MODEL
from django.db import models
from v1.point_systems.models import PointSystem
from v1.users.models import User


class MerchantManager(models.Manager):
    def create_merchant(self, **fields):
        pass


class Merchant(models.Model):
    objects = MerchantManager()

    user = models.OneToOneField(to=AUTH_USER_MODEL, primary_key=False, on_delete=models.CASCADE)
    company_id = models.BigAutoField(primary_key=True, unique=True)
    company_name = models.CharField(max_length=256)
    point_system = models.ForeignKey(to=PointSystem, primary_key=False, on_delete=models.PROTECT)


