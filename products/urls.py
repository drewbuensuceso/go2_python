# products/urls.py

from django.urls import path
from .views import available_product_list, out_of_stock_product_list, update_product_status, create_product

urlpatterns = [
    path('available/', available_product_list, name='available-product-list'),
    path('out-of-stock/', out_of_stock_product_list, name='out-of-stock-list'),
    path('update-status/<int:pk>/', update_product_status, name='product-status-update'),
    path('create/', create_product, name='product-create'),
]
