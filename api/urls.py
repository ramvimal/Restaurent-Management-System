from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path
from . import views

router = DefaultRouter()
router.register('menuitems', views.MenuItemsViewSet, basename='menuitems')
router.register('orders', views.OrdersViewSet, basename='orders')
router.register('category', views.CategoryViewSet, basename='category')
router.register('cart', views.CartViewSet, basename='cart')

urlpatterns = router.urls
