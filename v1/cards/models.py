from django.db import models


class CardManager(models.Manager):
    def create_card(self, **fields):
        card = self.model(**fields)
        card.save(using=self._db)

        return card


class Card(models.Model):
    objects = CardManager()

    card_id = models.BigAutoField(primary_key=True, unique=True)
    is_enabled = models.BooleanField()

