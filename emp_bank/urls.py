from . import views
from django.urls import path
from . views import NewAccountView, NewCardView

urlpatterns = [
    path('', views.dashboard, name='EMP-Bank-Home'),
    path('dashboard', views.dashboard, name='Employee-Dashboard'),
    path('revert', views.revert_notofi, name='Revert Notifications'),
    path('new_user', views.register, name='New User'),

    path('newAccount', NewAccountView.as_view(), name='new-Account'),
    path('newCard', NewCardView.as_view(), name='new-Card'),

    # path('transaction', views.transaction, namex='Transaction-Details'),
]
