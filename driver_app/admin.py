from django.contrib import admin

from .models import Driver, Vehicle


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name",
                    "created_at", "updated_at")
    search_fields = ("id", "first_name", "last_name",
                     "created_at", "updated_at")


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "driver",
        "make",
        "model",
        "plate_number",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "driver",
        "make",
        "model",
        "plate_number",
        "created_at",
        "updated_at",
    )
