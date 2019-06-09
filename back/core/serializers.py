from rest_framework import serializers
from .models import UsdPrice

class UsdPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsdPrice
        fields = ("clp_value", "date")
