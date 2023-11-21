from rest_framework import routers

from stock_app.views import ProductViewSet, StoreViewSet, ApiUserViewSet

router = routers.DefaultRouter()

urlpatterns = []


router.register('products', ProductViewSet)
router.register('stores', StoreViewSet)
router.register('users', ApiUserViewSet)


urlpatterns.extend(router.urls)
