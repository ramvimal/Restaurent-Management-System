from django.contrib import admin
from .models import Order , OrderItem 

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    
       
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "phone", "total_amount", "status", "created_at")
    list_filter=('id','customer_name','status', 'phone','total_amount','created_at')
    search_fields = ('id', 'customer_name')
    search_help_text = "Search order id or name"    
    inlines = [OrderItemInline]
   
    
    
