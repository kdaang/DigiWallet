from django.urls import path
from v1.stores.views import StoreRegister

app_name = 'stores'

urlpatterns = [
    path('register', StoreRegister.as_view()),
]