from django.db import models
from v1.merchants.models import Merchant


class StoreManager(models.Manager):
    def register(self, **fields):
        print(fields)
        store = self.model(**fields)
        store.save(using=self._db)

        return store


class Store(models.Model):
    objects = StoreManager()

    company = models.ForeignKey(to=Merchant, primary_key=False, on_delete=models.CASCADE)
    store_id = models.BigAutoField(primary_key=True, unique=True)

