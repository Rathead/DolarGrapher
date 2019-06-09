from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsdPriceViewSet

router = DefaultRouter()
router.register(r'usd_prices', UsdPriceViewSet)

urlpatterns = [
    path("", include(router.urls))
]
