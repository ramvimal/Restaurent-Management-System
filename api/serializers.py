from rest_framework import serializers
from menu.models import MenuItem
from orders.models import Order

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            "id",
            "name",
            "price",
            "description",
            "img_url",
            "category"
        ]

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "customer_name",
            "total_amount",
            "phone",
            "created_at",
            "status"
        ]
