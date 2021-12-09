import json

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase

from .models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializer


class DriverApiTestCase(APITestCase):
    def setUp(self):

        self.user = User.objects.create(username="test_user")
        self.driver_one = Driver.objects.create(
            first_name="first_name_1", last_name="last_name_1"
        )
        self.driver_two = Driver.objects.create(
            first_name="first_name_2", last_name="last_name_2"
        )
        self.driver_three = Driver.objects.create(
            first_name="first_name_3", last_name="last_name_3"
        )
        self.driver_four = Driver.objects.create(
            first_name="first_name_4", last_name="last_name_4"
        )
        self.driver_five = Driver.objects.create(
            first_name="first_name_5", last_name="last_name_5"
        )

    def test_get_driver_response_and_serializer(self):
        response = self.client.get(reverse("driver-list"))
        serializer_data = DriverSerializer(
            [
                self.driver_one,
                self.driver_two,
                self.driver_three,
                self.driver_four,
                self.driver_five,
            ],
            many=True,
        ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_data_filter_gte(self):
        response = self.client.get(
            reverse("driver-list") + "?created_at__gte=10-11-2021", format="json"
        )
        serializer_data = DriverSerializer(
            [
                self.driver_one,
                self.driver_two,
                self.driver_three,
                self.driver_four,
                self.driver_five,
            ],
            many=True,
        ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_data_filter_lte(self):
        response = self.client.get(
            reverse("driver-list") + "?created_at__lte=16-11-2021", format="json"
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual([], response.data)

    def test_create_driver(self):
        self.assertEqual(5, Driver.objects.all().count())
        data = {"first_name": "Firstname", "last_name": "Lastname"}
        response = self.client.post(
            reverse("driver-list"), data=data, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(6, Driver.objects.all().count())

    def test_update_driver(self):
        data = {"first_name": "Firstname", "last_name": "Lastname"}
        self.client.force_login(self.user)
        response = self.client.put(
            reverse("driver-detail", kwargs={"pk": self.driver_three.id}),
            data=data,
            format="json",
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.driver_three.refresh_from_db()
        self.assertEqual(data["first_name"], self.driver_three.first_name)

    def test_delete_driver(self):

        self.client.force_login(self.user)
        response = self.client.delete(
            reverse("driver-detail", kwargs={"pk": 4}))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(4, Driver.objects.all().count())

    def test_not_driver(self):
        response = self.client.get(reverse("driver-detail", kwargs={"pk": 25}))
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)


class VehiclesApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="test_user1")

        self.vehicle_one = Vehicle.objects.create(
            make="make_1", model="model_1", plate_number="plate_number_1",
        )
        self.vehicle_two = Vehicle.objects.create(
            make="make_2", model="model_2", plate_number="plate_number_2"
        )
        self.vehicle_three = Vehicle.objects.create(
            make="make_3", model="model_3", plate_number="plate_number_3"
        )

    def test_get_vehicle_response_and_serializer(self):
        response = self.client.get(reverse("vehicle-list"))
        serializer_data = VehicleSerializer(
            [self.vehicle_one, self.vehicle_two, self.vehicle_three], many=True
        ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create_vehicle(self):
        self.assertEqual(3, Vehicle.objects.all().count())
        data = {
            "make": "Make",
            "model": "Model",
            "plate_number": "АА 0001 ББ",
        }
        response = self.client.post(
            reverse("vehicle-list"), data=data, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Vehicle.objects.all().count())

    def test_update_vehicle(self):
        data = {
            "make": "Make",
            "model": "Model",
            "plate_number": "АА 0000 ББ",
        }
        self.client.force_login(self.user)
        response = self.client.put(
            reverse("vehicle-detail", kwargs={"pk": self.vehicle_three.id}),
            data=data,
            format="json",
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.vehicle_three.refresh_from_db()
        self.assertEqual(data["make"], self.vehicle_three.make)

    def test_delete_vehicle(self):

        self.client.force_login(self.user)
        response = self.client.delete(
            reverse("vehicle-detail", kwargs={"pk": 2}))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(2, Vehicle.objects.all().count())

    def test_with_vehicle_filter_yes(self):
        response = self.client.get(
            reverse("vehicle-list") + "?with_drivers=yes", format="json"
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual([], response.data)

    def test_with_drivers_filter_no(self):
        response = self.client.get(
            reverse("vehicle-list") + "?with_drivers=no", format="json"
        )
        serializer_data = VehicleSerializer(
            [
                self.vehicle_one,
                self.vehicle_two,
                self.vehicle_three,

            ],
            many=True,
        ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
