from . import views
from django.urls import path
from .views import AccountDetailView


urlpatterns = [
    # path('', AccountListView.as_view(), name='Bank-Home'),
    path('', views.home, name='Bank-Home'),
    path('account', views.account, name='Account-Details'),
    path('card', views.card, name='Card-Details'),
    path('transaction', views.transaction, name='Transaction-Details'),

    path('account/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
]
