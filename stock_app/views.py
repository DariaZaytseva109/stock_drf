from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from stock_app.models import Product, Store, UserGroup, \
    ApiUser, ProductInStore
from stock_app.serializers import ProductSerializer, StoreSerializer, \
    UserGroupSerializer, UserSerializer, ProductInStoreSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductInStoreViewSet(viewsets.ModelViewSet):
    queryset = ProductInStore.objects.all()
    serializer_class = ProductInStoreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(
        detail=True,
        methods=['put', 'get'],
        name='Поставить продукты на склад',
        permission_classes=[]
    )
    def deliver_products(self, request, pk=None):
        store = get_object_or_404(Store.objects.all(), id=pk)
        serializer = ProductInStoreSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            delivered_quantity = serializer.validated_data['quantity']
            delivered_product_name = serializer.validated_data['product']["name"]
            delivered_product = Product.objects.get(name=delivered_product_name)
            ProductInStore.objects.create(product=delivered_product, store=store, quantity=delivered_quantity)
            return Response({'status': 'Продукт поставлен'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ApiUserViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]