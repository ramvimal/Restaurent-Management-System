from rest_framework.decorators import api_view
from rest_framework.response import Response
from menu.models import MenuItem , Category
from .serializers import MenuItemSerializer , OrdersSerializer , CategorySerializer
from orders.models import Order
from rest_framework import viewsets
from rest_framework.views import APIView



class MenuItemsViewSet(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()


class OrdersViewSet(viewsets.ModelViewSet):
    serializer_class = OrdersSerializer
    queryset = Order.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class cartApiView(APIView):
    def get(self,request):
        print("Session key : ", request.session.session_key)
        print("Session data : ", request.session.items())
        cart = request.session.get("cart",{})
        return Response(cart)
    
    def post(self, request):
        cart = request.session.get("cart", {})  
        cart["1"] = 2   # example item
        request.session["cart"] = cart
        request.session.modified = True
        return Response({"message": "cart updated"})