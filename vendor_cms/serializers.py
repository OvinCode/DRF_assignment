from rest_framework import serializers
from .models import Order,Vendor,Performance


class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = "__all__"


    def put(self, instance, validated_data):
        validated_data.pop('vendor_code', None)  # Remove 'vendor_code' from validated data
        return super().update(instance, validated_data)


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"


class PerformanceSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Performance
        fields = "__all__"