from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.menu_list_api, name="api_menu"),
    path("orders/", views.order_list_api, name="orders_list"),
]
