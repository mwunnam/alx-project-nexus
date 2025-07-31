from rest_framework import serializers
from .models import Order, OrderItem
from products_app.serializer import ProductSerialiazer
from users_app.serializer import UserSerializer

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class meta:
        model = Order
        fields = ['shipping_address', 'total_price', 'status', 'created_at']

class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    product = ProductSerializer()

    class meta:
        model = OrderItem
        fields = ['quantity', 'price']
