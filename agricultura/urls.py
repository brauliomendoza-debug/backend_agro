from rest_framework.routers import DefaultRouter
from .views import AgricultorViewSet, ProductoAgricolaViewSet

router = DefaultRouter()

router.register(
    'agricultores',
    AgricultorViewSet
)

router.register(
    'productos',
    ProductoAgricolaViewSet
)

urlpatterns = router.urls