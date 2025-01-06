

from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_price', 'created_at', 'status']
        read_only_fields = ['id', 'user', 'created_at', 'status'] 
