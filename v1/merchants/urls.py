from django.urls import path
from v1.merchants.views import MerchantView

app_name = 'merchants'

urlpatterns = [
    path('', MerchantView.as_view())
]