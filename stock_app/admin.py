from django.contrib import admin

from stock_app.models import Product, Store


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


admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Склады"

