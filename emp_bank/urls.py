from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='EMP-Bank-Home'),
    path('dashboard', views.dashboard, name='Employee-Dashboard'),
    path('revert', views.revert_notofi, name='Revert Notifications'),
    # path('transaction', views.transaction, namex='Transaction-Details'),
]
