
from .models import (
    Product,
    Order,
    OrderItem
    )
from rest_framework import serializers
from django.db import transaction


        
        
class ProductSerializer(serializers.ModelSerializer):
    
    
    
    class Meta:
        model = Product
        fields = "__all__"  
        
        
class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)
    product_name = serializers.ReadOnlyField(source="product.name")

    class Meta:
        model = OrderItem
        fields = [
            "product_id",
            "product_name",
            "quantity",
            "price"
        ]   
        
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "total_price",
            "items",
            "created_at"
        ]
    def create(self, validated_data):
        items_data = validated_data.pop("items")
        user =self.context["request"].user
        
        with transaction.Atomic():
            order = Order.objects.create(user=user)
            total = 0
            
            for item in items_data:
                product = Product.objects.get(id=item["product_id"])
                quantity = item["quantity"]
                price = product.price 
                
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=price
                )
                
                total += price * quantity
            order.total_price = total
            order.save()
        return order                            