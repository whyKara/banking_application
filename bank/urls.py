from . import views
from django.urls import path
from .views import AccountDetailView,NewTransactionView


urlpatterns = [
    # path('', AccountListView.as_view(), name='Bank-Home'),
    path('', views.home, name='Bank-Home'),
    path('account', views.account, name='Accounts'),
    path('card', views.card, name='Card-Details'),
    path('transaction', views.transaction, name='Transaction-Details'),

    path('newTransaction', NewTransactionView.as_view(), name='new-Transaction'),
    path('account/<pk>/', AccountDetailView.as_view(), name='account-detail'),
]
