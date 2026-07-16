from abc import ABC, abstractmethod
from ParkingLot.enums.VehicleType import VehicleType

class Vehicle(ABC):
    def __init__(self,license_plate : str,vehicle_type : VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    @abstractmethod
    def get_vehicle_type(self):
        pass

    @abstractmethod
    def get_license_plate(self):
        pass

class Car(Vehicle):
    def __init__(self, license_plate, vehicle_type):
        super().__init__(license_plate, vehicle_type)

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_license_plate(self):
        return self.license_plate
    

class Motorcycle(Vehicle):
    def __init__(self, license_plate, vehicle_type):
        super().__init__(license_plate, vehicle_type)

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_license_plate(self):
        return self.license_plate
    
class Truck(Vehicle):
    def __init__(self, license_plate, vehicle_type):
        super().__init__(license_plate, vehicle_type)

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_license_plate(self):
        return self.license_plate
