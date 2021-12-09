from rest_framework import serializers

from .models import Driver, Vehicle


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "id", "first_name", "last_name"


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "make", "model", "plate_number", "driver"


class SetDriverSerializer(serializers.Serializer):
    driver = serializers.PrimaryKeyRelatedField(
        queryset=Driver.objects.all(), allow_null=True
    )
