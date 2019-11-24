from django.urls import path
from v1.transactions.views import PostMerchantTransaction, GetTransaction

app_name = 'transactions'

urlpatterns = [
    path('post', PostMerchantTransaction.as_view()),
    path('get', GetTransaction.as_view())
]