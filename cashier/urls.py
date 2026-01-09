from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.cashier_login, name="cashier_login"),
    path('dashboard/', views.cashier_dashboard, name='cashier_dashboard'),
    path("logout/", views.cashier_logout, name="cashier_logout"),
    path("order/<int:order_id>/", views.cashier_order_detail, name="cashier_order_detail"),
]
