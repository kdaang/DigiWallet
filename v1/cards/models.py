from django.db import models


# Create your models here.
class Card(models.Model):
    card_id = models.BigAutoField(primary_key=True, unique=True)
    is_enabled = models.BooleanField()



