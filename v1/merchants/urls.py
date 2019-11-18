from django.urls import path
from v1.merchants.views import MerchantSignup

app_name = 'merchants'

urlpatterns = [
    path('signup', MerchantSignup.as_view())
]