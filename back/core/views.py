from rest_framework import viewsets
from .serializers import UsdPriceSerializer
from .models import UsdPrice

class UsdPriceViewSet(viewsets.ModelViewSet):
    serializer_class = UsdPriceSerializer
    queryset = UsdPrice.objects.all()
