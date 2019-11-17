from django.db import models
from DigiWallet.settings import AUTH_USER_MODEL


class EmployeeManager(models.Manager):
    def create_employee(self, **fields):
        pass


class Employee(models.Model):
    objects = EmployeeManager()

    user = models.OneToOneField(to=AUTH_USER_MODEL, primary_key=False, on_delete=models.CASCADE)
    employee_id = models.BigAutoField(primary_key=True, unique=True)
    # TODO: EMPLOYEE DETAILS

