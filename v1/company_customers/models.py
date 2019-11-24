from django.db import models
from v1.customers.models import Customer
from v1.merchants.models import Merchant


class CompanyCustomerManager(models.Manager):
    def create_company_customer_data(self, **fields):
        company_customer = self.model(**fields)
        company_customer.save(using=self._db)

        return company_customer

    def get_or_create_company_customer(self, **fields):
        company_customer = self.get_or_create(company_id=fields['company'], customer_id=fields['customer'])

        return company_customer[0]
1


class CompanyCustomer(models.Model):
    objects = CompanyCustomerManager()

    company = models.ForeignKey(to=Merchant, primary_key=False, on_delete=models.CASCADE)
    customer = models.ForeignKey(to=Customer, primary_key=False, on_delete=models.CASCADE)
    points = models.BigIntegerField(default=0)
