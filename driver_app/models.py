from django.db import models


class TimeMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего обновления"
    )

    class Meta:
        abstract = True


class Driver(TimeMixin, models.Model):
    first_name = models.CharField(max_length=35, verbose_name="Имя")
    last_name = models.CharField(max_length=35, verbose_name="Фамилия")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Vehicle(TimeMixin, models.Model):
    driver = models.ForeignKey(
        "Driver",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Водитель",
    )
    make = models.CharField(max_length=50, verbose_name="Бренд")
    model = models.CharField(max_length=50, verbose_name="Модель")

    plate_number = models.CharField(
        max_length=10, verbose_name="Номер Машины", unique=True
    )

    def __str__(self):
        return self.model
