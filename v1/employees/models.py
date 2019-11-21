from django.db import models
from django.conf import settings
from v1.stores.models import Store
from v1.users.models import User, UserTypes


class EmployeeManager(models.Manager):
    def create_employee(self, **fields):
        employee = self.model(**fields)
        employee.save(using=self._db)

        return employee

    def signup(self, **fields):
        user_data = fields.pop('user')
        user_data['user_type'] = UserTypes.EMPLOYEE
        user = User.objects.create_user(**user_data)
        employee = self.create(user=user, **fields)
        employee.save(using=self._db)

        return employee


class Employee(models.Model):
    objects = EmployeeManager()

    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=False, on_delete=models.CASCADE)
    employee_id = models.BigAutoField(primary_key=True, unique=True)
    store = models.ForeignKey(to=Store, primary_key=False, on_delete=models.SET_NULL, null=True, blank=True)
    # TODO: EMPLOYEE DETAILS

