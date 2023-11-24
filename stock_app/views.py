from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from stock_app.models import Product, Store, UserGroup, \
    ApiUser, ProductInStore
from stock_app.serializers import ProductSerializer, StoreSerializer, \
    UserGroupSerializer, UserSerializer, \
    ProductInStoreSerializer, SimpleProductInStoreSerializer


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
        permission_classes=[],
        serializer_class=SimpleProductInStoreSerializer
    )
    def supply(self, request, pk=None):
        store = Store.objects.get(pk=pk)
        print(store)
        if request.method == 'GET':
            return Response({})
        product = Product.objects.get(id=request.data['product'])

        quantity = int(request.data['quantity'])
        print(product, quantity)
        products_in_store = ProductInStore.objects.filter(store=store)
        print(products_in_store)
        for prod in products_in_store:
            print(prod.product)
            if prod.product == product:
                store.add_to_existing_product(prod, quantity)
                return Response({'status': 'product supplied'})
        store.add_new_product(product, quantity)
        return Response({'status': 'product added'})


class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ApiUserViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

