from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2 )
    description = models.TextField()

    created_at  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.id}:{self.user}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="items"
    )    
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )  
    
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity} * {self.price}"  
