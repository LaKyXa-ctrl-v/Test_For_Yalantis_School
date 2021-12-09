from types import MethodType

from django.urls.conf import include, path
from rest_framework import routers

from driver_app import api

from .api import DriverViewSet, SetDriverSerializer, VehicleViewSet
from .models import Driver, Vehicle

router = routers.DefaultRouter()
router.register("drivers/driver", DriverViewSet, "driver")
router.register("vehicles/vehicle", VehicleViewSet, "vehicle")


urlpatterns = [
    path("", include(router.urls)),
    path("vehicles/vehicle/set_driver/<vehicle_id>", api.SetDriverView.as_view()),
]
