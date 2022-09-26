from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='Bank-Home'),
    path('account', views.account, name='Account-Details'),
    path('card', views.card, name='Card-Details'),
]
