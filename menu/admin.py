from django.contrib import admin
from .models import Category, MenuItem

@admin.register((MenuItem))
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('category','name','price','available')
    list_filter=('category','name','price','available')
    search_fields = ('id', 'name')
    search_help_text = "Searhch order id or name" 
    def has_module_permission(self, request):
        return request.user.groups.filter(name="Manager").exists()

    def has_view_permission(self, request, obj=None):
        return request.user.groups.filter(name="Manager").exists()

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name="Manager").exists()

    def has_add_permission(self, request):
        return request.user.groups.filter(name="Manager").exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name="Manager").exists()


@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    
    def has_module_permission(self, request):
        return request.user.groups.filter(name="Manager").exists()

    def has_view_permission(self, request, obj=None):
        return request.user.groups.filter(name="Manager").exists()

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name="Manager").exists()

    def has_add_permission(self, request):
        return request.user.groups.filter(name="Manager").exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name="Manager").exists()

