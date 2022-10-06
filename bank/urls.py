from . import views
from django.urls import path
from .views import (
    AccountListView,
    AccountDetailView,
    AccountCreateView,
    AccountUpdateView
)

urlpatterns = [
    path('', AccountListView.as_view(), name='Bank-Home'),
    path('account', views.account, name='Account-Details'),
    path('card', views.card, name='Card-Details'),
    path('transaction', views.transaction, name='Transaction-Details'),

    path('account/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('account/new/', AccountCreateView.as_view(), name='account-create'),
    path('account/<int:pk>/update/', AccountUpdateView.as_view(), name='account-update'),
]
