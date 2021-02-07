from django.urls import path
from .views import *

urlpatterns = [
    path('', EquipList.as_view(), name='equip_list'),
    path('add/', EquipAdd.as_view(), name='equip_add'), 
    path('<int:pk>/', EquipView.as_view(), name='equip_view'),
    path('<int:pk>/edit/', EquipEdit.as_view(), name='equip_edit'),
    path('<int:pk>/delete/', EquipDelete.as_view(), name='equip_delete'),
]