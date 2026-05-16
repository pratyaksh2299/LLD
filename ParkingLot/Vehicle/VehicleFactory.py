import re

from .Vehicle import Vehicle
from .CarVehicle import CarVehicle
from .BikeVehicle import BikeVehicle
from .TruckVehicle import TruckVehicle
class VehicleFactory:

    @staticmethod
    def create_vehicle(vehicle_type, licence_plate, fee_strategy) -> Vehicle:
        if vehicle_type =="Car":
            vehicle : Vehicle = CarVehicle(licence_plate, fee_strategy)
            return vehicle
        elif vehicle_type =="Bike":
            vehicle : Vehicle = BikeVehicle(licence_plate, fee_strategy)
            return vehicle
        elif vehicle_type =="Truck":
            vehicle : Vehicle = TruckVehicle(licence_plate, fee_strategy)
            return vehicle
        else:
            raise ValueError("Invalid vehicle type")
         