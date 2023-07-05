from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView, DemoView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>', ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/demo/', DemoView.as_view(), name='demo'),
]