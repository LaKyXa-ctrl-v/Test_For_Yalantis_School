from distutils.util import strtobool

import django_filters
from rest_framework import permissions, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Driver, Vehicle
from .serializers import DriverSerializer, SetDriverSerializer, VehicleSerializer


class DateDriverFilter(django_filters.FilterSet):
    created_at__gte = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte", input_formats=["%d-%m-%Y"]
    )
    created_at__lte = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="lte", input_formats=["%d-%m-%Y"]
    )

    class Meta:
        model = Driver
        fields = ["created_at__gte", "created_at__lte"]


class VehicleFilter(django_filters.FilterSet):
    with_drivers = django_filters.TypedChoiceFilter(
        field_name="driver",
        choices=(("no", "Without driver"),
                 ("yes", "With a driver"), ("", "All")),
        coerce=strtobool,
        lookup_expr="isnull",
        exclude=True,
    )

    class Meta:
        model = Vehicle
        fields = ["with_drivers"]


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DriverSerializer
    filterset_class = DateDriverFilter


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VehicleSerializer
    filterset_class = VehicleFilter


class VehicleViewSet(viewsets.ModelViewSet):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    filterset_class = VehicleFilter


class SetDriverView(CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = SetDriverSerializer
    lookup_url_kwarg = "vehicle_id"
    lookup_field = "id"

    def create(self, request):
        vehicle = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        vehicle.driver_id = serializer.data["driver"]
        vehicle.save()

        return Response(VehicleSerializer(instance=vehicle).data)
