from django.urls import path
from v1.customers.views import CustomerSignup

app_name = 'customers'

urlpatterns = [
    path('signup', CustomerSignup.as_view())
]