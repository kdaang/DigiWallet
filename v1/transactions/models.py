from django.db import models, transaction
from django.conf import settings
from rest_framework.exceptions import ValidationError

from v1.company_customers.models import CompanyCustomer
from v1.company_customers.serializers import CompanyCustomerSerializer
from v1.point_systems.models import PointSystem


class TransactionManager(models.Manager):
    def create_transaction(self, **fields):
        transaction = self.model(**fields)
        # transaction.save(using=self._db)

        return transaction

    @transaction.atomic
    def create_merchant_transaction(self, **fields):
        point_system = PointSystem.objects.get(pk=fields['from_user'].pk)

        if point_system.is_enabled:
            fields['total'] = fields['total']*100*point_system.points_per_cent

        company_customer = CompanyCustomer.objects.get_or_create_company_customer(
            company=fields['from_user'].get_merchant(), customer=fields['to_user'].get_customer())
        company_customer_serializer = CompanyCustomerSerializer(company_customer, data={'points': fields['total']},
                                                                partial=True)
        company_customer_serializer.is_valid(raise_exception=True)
        company_customer_serializer.save()

        return self.create_transaction(**fields)

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
