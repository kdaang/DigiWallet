"""DigiWallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/merchants/', include('v1.merchants.urls', namespace='v1:merchants')),
    path('api/v1/stores/', include('v1.stores.urls', namespace='v1:stores')),
    path('api/v1/customers/', include('v1.customers.urls', namespace='v1:customers')),
    path('api/v1/employees/', include('v1.employees.urls', namespace='v1:employees')),
    path('api/v1/transactions/', include('v1.transactions.urls', namespace='v1:transactions'))
]
