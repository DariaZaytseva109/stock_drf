from rest_framework import serializers

from stock_app.models import Store, Product, ProductInStore


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'address', 'products']
        read_only_fields = ['id']
        depth = 3


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']
        read_only_fields = ['id']


class ProductInStoreSerializer(serializers.Serializer):
    class Meta:
        model = ProductInStore
        fields = ['id', 'product', 'quantity']
        read_only_fields = ['id']

