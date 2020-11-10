from django.urls import path, include
from . import views

urlpatterns=[
    path("",views.sale_percentage, name = 'sale_percentage'),
    path("sale",views.total_sale_percent, name = 'total_sale_percent'),
    path("price", views.total_price_percentage, name = 'total_price_percentage')
    ]