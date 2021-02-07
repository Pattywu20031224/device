from django.urls import path
from .views import *

urlpatterns = [
    path('', LogList.as_view(), name='log_list'),
    path('checkout/', CheckoutBorrower.as_view(), name='checkout_borrower'), 
    path('checkout/<int:rid>/', CheckoutEquip.as_view(), name='checkout_equip'), 
    path('checkout/<int:rid>/<int:bid>/', CheckoutLog.as_view(), name='checkout_log'),
    path('return/', ReturnEquip.as_view(), name='return_equip'), 
    path('return/<int:lid>/', ReturnLog.as_view(), name='return_log'),
]