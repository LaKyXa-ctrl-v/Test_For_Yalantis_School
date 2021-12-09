# Test_for_Yalantis
### You can use [Postman](https://www.postman.com/) or [Swagger](http://127.0.0.1:8000/swagger/)
# Driver:

+ GET /drivers/driver/ - output of the list of drivers
+ GET /drivers/driver/?created_at__gte=10-11-2021 - output of the list of drivers created after 10-11-2021
+ GET /drivers/driver/?created_at__lte=16-11-2021 - output of the list of drivers created before 16-11-2021

+ GET /drivers/driver/<driver_id>/ - obtaining information on a particular driver
+ POST /drivers/driver/ - creating a new driver
+ UPDATE /drivers/driver/<driver_id>/ - driver editing
+ DELETE /drivers/driver/<driver_id>/ - driver removal

# Vehicle:

+ GET /vehicles/vehicle/ - output of the list of machines
+ GET /vehicles/vehicle/?with_drivers=yes - output of the list of cars with drivers
+ GET /vehicles/vehicle/?with_drivers=no - output of the list of cars without drivers

+ GET /vehicles/vehicle/<vehicle_id> - obtaining information on a specific machine
+ POST /vehicles/vehicle/ - creating a new machine
+ UPDATE /vehicles/vehicle/<vehicle_id>/ - machine editing
+ POST /vehicles/set_driver/<vehicle_id>/ - put the driver in the car / get the driver out of the car  
+ DELETE /vehicles/vehicle/<vehicle_id>/ - removing the machine



### This project was created for a test assignment to a school. 
### It does not carry any semantic meaning. 
##### Whoever reads this good luck to you!