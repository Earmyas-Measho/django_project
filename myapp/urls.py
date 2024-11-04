from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.member_list, name='member_list'),
    path('items/', views.item_list, name='item_list'),
    path('contracts/', views.contract_list, name='contract_list'),
]
