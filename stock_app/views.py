from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from stock_app.models import Product, Store
from stock_app.serializers import ProductSerializer, StoreSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]