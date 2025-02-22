from django.conf import settings
from django.db import models
from v1.point_systems.models import PointSystem
from v1.users.models import User, UserTypes


class MerchantManager(models.Manager):
    def create_merchant(self, user, point_system, **fields):
        merchant = self.model(user=user, point_system=point_system, company_name=fields['company_name'])
        merchant.save(using=self._db)

        return merchant

    def signup(self, **fields):
        user_data = fields.pop('user')
        user_data['user_type'] = UserTypes.MERCHANT
        point_system_data = fields.pop('point_system')
        user = User.objects.create_user(**user_data)
        point_system = PointSystem.objects.create_point_system(**point_system_data)
        merchant_user = self.create_merchant(user=user, point_system=point_system, **fields)

        return merchant_user


class Merchant(models.Model):
    objects = MerchantManager()

    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=False, on_delete=models.CASCADE)
    company_id = models.BigAutoField(primary_key=True, unique=True)
    company_name = models.CharField(max_length=256)
    point_system = models.ForeignKey(to=PointSystem, primary_key=False, on_delete=models.PROTECT)




