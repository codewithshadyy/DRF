from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product, Category
from .serializers import CategorySerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsSellerOrAdminOrReadOnly


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]   
    filterset_fields = ["category" ]
    permission_classes = [IsSellerOrAdminOrReadOnly]
