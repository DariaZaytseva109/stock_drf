from rest_framework import routers

from stock_app.views import ProductViewSet, StoreViewSet

router = routers.DefaultRouter()

urlpatterns = []


router.register('products', ProductViewSet)
router.register('stores', StoreViewSet)


urlpatterns.extend(router.urls)
