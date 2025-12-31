from django.contrib import admin
from .models import Order , OrderItem

# Register your models here.
@admin.register(Order)
class Orderadmin(admin.ModelAdmin):
    list_display = ('customer_name', 'total_amount','is_paid','created_at')
    list_filter=('customer_name', 'total_amount','is_paid','created_at')

@admin.register(OrderItem)
class OrderItemadmin(admin.ModelAdmin):
    list_display = ('order', 'item_name','price','quantity')
    list_filter=('order', 'item_name','price','quantity')