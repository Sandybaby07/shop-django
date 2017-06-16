from django.contrib import admin
from mysite.models import Product, Category, Order, OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'sku', 'name', 'stock', 'price')
    ordering = ('category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
