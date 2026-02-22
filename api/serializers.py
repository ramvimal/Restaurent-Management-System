from rest_framework import serializers
from menu.models import MenuItem , Category
from orders.models import Order , OrderItem

class MenuItemSerializer(serializers.ModelSerializer):

    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True
    )

    category_name =  serializers.StringRelatedField(
        source="category",
        read_only=True
    )
    
    class Meta:
        model = MenuItem
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):

    customer_name = serializers.StringRelatedField(
        source="order.customer_name",
        read_only=True
    )

    order = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(),
        write_only=True
    )
    class Meta:
        model = OrderItem
        fields = "__all__"
