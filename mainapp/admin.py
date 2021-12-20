from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    change_form_template = 'custom_admin/change_form.html'
    search_fields = ['title', 'price']
    list_display = ['category', 'title', 'slug', 'price']
    list_filter = ['category', 'title', 'slug', 'price']

class OrderAdmin(admin.ModelAdmin):
    change_form_template = 'custom_admin/change_form.html'
    search_fields = ['first_name', 'last_name', 'phone',]
    list_display = ['customer', 'first_name', 'last_name', 'phone', 'address', 'status', 'created_at', 'order_date']
    list_filter = ['customer', 'first_name', 'last_name', 'phone', 'address', 'status', 'created_at', 'order_date']

class CustomerAdmin(admin.ModelAdmin):
    change_form_template = 'custom_admin/change_form.html'
    search_fields = ['phone', 'address']
    list_display = ['user', 'phone', 'address']
    list_filter = ['user', 'phone', 'address']

class CategoryAdmin(admin.ModelAdmin):
    change_form_template = 'custom_admin/change_form.html'
    search_fields = ['name', 'slug']
    list_display = ['name', 'slug']
    list_filter = ['name', 'slug']

class CartAdmin(admin.ModelAdmin):
    change_form_template = 'custom_admin/change_form.html'
    search_fields = ['final_price']
    list_display = ['owner', 'total_products', 'final_price', 'in_order', 'for_anonymous_user']
    list_filter = ['owner', 'total_products', 'final_price', 'in_order', 'for_anonymous_user']

class CartProductAdmin(admin.ModelAdmin):
    change_form_template = 'custom_admin/change_form.html'
    list_display = ['user', 'cart', 'product', 'qty', 'final_price']
    list_filter = ['user', 'cart', 'product', 'qty', 'final_price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(CartProduct, CartProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)

