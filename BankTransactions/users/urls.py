from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path("",views.bank_balance, name = 'bank_balance'),
    path("<int:pk>/",views.user_balance, name= 'user_balance'),
    path("count/",views.transaction_count, name = 'user_count')
]