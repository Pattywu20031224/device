from django.urls import path
from .views import *

urlpatterns = [
    path('', BorrowerList.as_view(), name='borrower_list'), 
    path('add/', BorrowerAdd.as_view(), name='borrower_add'),
    path('<int:pk>/', BorrowerView.as_view(), name='borrower_view'), 
    path('<int:pk>/edit/', BorrowerEdit.as_view(), name='borrower_edit'),
    path('<int:pk>/delete/',BorrowerDelete.as_view(), name='borrower_delete'),
]