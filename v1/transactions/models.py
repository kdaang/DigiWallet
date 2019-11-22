from django.db import models
from django.conf import settings


class TransactionManager(models.Manager):
    def create_transaction(self, **fields):
        transaction = self.model(**fields)
        transaction.save(using=self._db)

        return transaction

    def get_transactions(self, **fields):
        user_pk = fields['user']
        transactions = (Transaction.objects.filter(from_user=user_pk) | Transaction.objects.filter(to_user=user_pk))\
            .order_by('-date_created')

        return transactions


class Transaction(models.Model):
    objects = TransactionManager()
    transaction_id = models.BigAutoField(primary_key=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, primary_key=False, on_delete=models.PROTECT,
                                  related_name='from_user')
    to_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, primary_key=False, on_delete=models.PROTECT,
                                related_name='to_user')
    total = models.BigIntegerField()
