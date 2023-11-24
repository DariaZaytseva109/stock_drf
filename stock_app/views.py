from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from stock_app.models import Product, Store, UserGroup, \
    ApiUser, ProductInStore
from stock_app.permissions import IsConsumerPermission, IsSupplierPermission
from stock_app.serializers import ProductSerializer, StoreSerializer, \
    UserGroupSerializer, UserSerializer, \
    SimpleProductInStoreSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(
        detail=True,
        methods=['put'],
        name='Поставить продукты на склад',
        permission_classes=[IsSupplierPermission],
        serializer_class=SimpleProductInStoreSerializer
    )
    def supply(self, request, pk=None):
        store = Store.objects.get(pk=pk)
        product = Product.objects.get(id=request.data['product'])
        quantity = int(request.data['quantity'])
        products_in_store = ProductInStore.objects.filter(store=store)
        for prod in products_in_store:
            if prod.product == product:
                store.add_to_existing_product(prod, quantity)
                return Response({'status': 'product supplied'})
        store.add_new_product(product, quantity)
        return Response({'status': 'new product supplied'})

    @action(
        detail=True,
        methods=['put'],
        name='Забрать продукты со склада',
        permission_classes=[IsConsumerPermission],
        serializer_class=SimpleProductInStoreSerializer
    )
    def consume(self, request, pk=None):
        store = Store.objects.get(pk=pk)
        product = Product.objects.get(id=request.data['product'])
        quantity = int(request.data['quantity'])
        products_in_store = ProductInStore.objects.filter(store=store)
        for prod in products_in_store:
            if prod.product == product:
                if prod.quantity < quantity:
                    return Response({'status': 'insufficient product at store'})
                elif prod.quantity == quantity:
                    prod.delete()
                    return Response({'status': 'product consumed'})
                else:
                    prod.quantity = prod.quantity - quantity
                    prod.save()
                    return Response({'status': 'product consumed'})
        return Response({'status': 'no such product'})


class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ApiUserViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

