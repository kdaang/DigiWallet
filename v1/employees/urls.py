from django.urls import path
from v1.employees.views import EmployeeSignup

app_name = 'employees'

urlpatterns = [
    path('signup', EmployeeSignup.as_view())
]