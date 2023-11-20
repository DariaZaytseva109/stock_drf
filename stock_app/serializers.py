from rest_framework import serializers

from stock_app.models import Store, Product, ProductInStore


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']
        read_only_fields = ['id']


class ProductInStoreSerializer(serializers.Serializer):
    product = ProductSerializer()
    quantity = serializers.IntegerField()

    class Meta:
        model = ProductInStore
        fields = ['product', 'quantity']
        read_only_fields = ['id']


class StoreSerializer(serializers.ModelSerializer):
    products = ProductInStoreSerializer(many=True)

    class Meta:
        model = Store
        fields = ['id', 'name', 'address', 'products']
        read_only_fields = ['id']

