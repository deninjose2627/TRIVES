from django.contrib import admin 
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email')  # Add 'email' to the list display

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(OrderItem)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['fullname', 'address', 'postal_code']

from django.contrib import admin
from .models import Supplier

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'username', 'email', 'address']
    search_fields = ['company_name', 'username', 'email']
    readonly_fields = ['password']  # Don't allow editing password in admin

admin.site.register(Supplier, SupplierAdmin)

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'order_date') 