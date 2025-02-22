from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.template.defaultfilters import upper


class UserTypes:
    CUSTOMER = 'CUSTOMER'
    MERCHANT = 'MERCHANT'
    EMPLOYEE = 'EMPLOYEE'
    ADMIN = 'ADMIN'

    choices = [
        (CUSTOMER, 'Customer'),
        (MERCHANT, 'Merchant'),
        (EMPLOYEE, 'Employee'),
        (ADMIN, 'ADMIN')
    ]


class UserManager(BaseUserManager):
    def create_user(self, email, user_type, first_name, last_name, password, **extra_fields):
        email = self.normalize_email(email)
        first_name = upper(first_name)
        last_name = upper(last_name)

        user = self.model(email=email, user_type=user_type, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, user_type=UserTypes.ADMIN,
                         first_name='admin', last_name='admin', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(user_type=user_type, first_name=first_name, last_name=last_name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    user_id = models.BigAutoField(primary_key=True, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    user_type = models.CharField(max_length=256, choices=UserTypes.choices)
    date_created = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = []

    def get_merchant(self):
        if self.user_type == UserTypes.MERCHANT:
            return self.merchant
        elif self.user_type == UserTypes.EMPLOYEE:
            return self.employee.get_merchant()
        else:
            return None

    def get_customer(self):
        if self.user_type == UserTypes.CUSTOMER:
            return self.customer
        else:
            return None
