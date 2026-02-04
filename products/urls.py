

from .views import ProductListAPIView, ProductDetailAPIView, OrderListCreateView
from django.urls import path

urlpatterns = [
    path("products/",  ProductListAPIView.as_view(), name = "product-list"),
    path("products/<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
    path("order/", OrderListCreateView.as_view(), name="orders")
]



