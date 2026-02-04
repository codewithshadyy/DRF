from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import (Product,Order )
from .serializers import  (ProductSerializer, OrderItemSerializer, OrderSerializer)
# from django_filters.rest_framework import DjangoFilterBackend
# from .permissions import IsSellerOrAdminOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated



# # class CategoryViewSet(ModelViewSet):
# #     queryset = Category.objects.all()
# #     serializer_class = CategorySerializer
    
# # class ProductViewSet(ModelViewSet):
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer
# #     filter_backends = [DjangoFilterBackend]   
# #     filterset_fields = ["category" ]
# #     permission_classes = [IsSellerOrAdminOrReadOnly]

class ProductListAPIView(APIView):
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProductDetailAPIView(APIView):
    
    
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)  
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
         

class OrderListCreateView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)