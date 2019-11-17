from django.urls import path
from v1.cards.views import CardView

app_name = 'cards'

urlpatterns = [
    path('', CardView.as_view()),
]