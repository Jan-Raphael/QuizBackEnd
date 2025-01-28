# products/urls.py
from django.urls import path
from .views import GetProducts, GetProduct

urlpatterns = [
    path('products/', GetProducts.as_view(), name='get_products'),
    path('products/<uuid:pk>/', GetProduct.as_view(), name='get_product'),
]
