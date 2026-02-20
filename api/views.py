from rest_framework.decorators import api_view
from rest_framework.response import Response
from menu.models import MenuItem , Category
from .serializers import MenuItemSerializer , OrdersSerializer , CategorySerializer
from orders.models import Order
from rest_framework import viewsets



class MenuItemsViewSet(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()


class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersSerializer
    queryset = Order.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()