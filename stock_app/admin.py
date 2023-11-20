from django.contrib import admin

from stock_app.models import Product, Store, ProductInStore


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'id')
    list_display_links = ('name', )
    ordering = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    ordering = ['name']


@admin.register(ProductInStore)
class ProductInStoreAdmin(admin.ModelAdmin):
    list_display = ('store', 'product', 'quantity')
    list_display_links = ('store', )
    ordering = ['store']


admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Склады"

