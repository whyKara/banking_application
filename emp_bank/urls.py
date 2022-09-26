from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='EMP-Bank-Home'),
    path('dashboard', views.dashboard, name='Employee-Dashboard'),
    # path('card', views.card, name='Card-Details'),
    # path('transaction', views.transaction, name='Transaction-Details'),
]
