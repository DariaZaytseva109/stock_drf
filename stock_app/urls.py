from rest_framework import routers

from stock_app.views import ProductViewSet, StoreViewSet, \
    ApiUserViewSet, ProductInStoreViewSet

router = routers.DefaultRouter()

urlpatterns = []


router.register('products', ProductViewSet)
router.register('stores', StoreViewSet)
router.register('users', ApiUserViewSet)
router.register('products_in_store', ProductInStoreViewSet)


urlpatterns.extend(router.urls)
