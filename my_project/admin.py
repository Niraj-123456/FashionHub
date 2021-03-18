from django.contrib import admin
from .models import Product, Category, Order, OrderItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'img_path', 'price', 'category_id', 'added_date', 'updated_at']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'img_path', 'added_date', 'updated_at']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'transaction_id', 'completed', 'delivered', 'date_ordered']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
