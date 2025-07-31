from django.db import models
from users_app.models import User
from products_app.models import Product

class Order(models.Model):
    user = models.Foreignkey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')])
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.Foreignkey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_place=2)

