from django.urls import path
from v1.transactions.views import PostTransaction, GetTransaction

app_name = 'transactions'

urlpatterns = [
    path('post', PostTransaction.as_view()),
    path('get', GetTransaction.as_view())
]