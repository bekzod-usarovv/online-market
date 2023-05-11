from rest_framework.routers import SimpleRouter
from .views import CategoryViewSet, ProductViewSet

router = SimpleRouter()

router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)

