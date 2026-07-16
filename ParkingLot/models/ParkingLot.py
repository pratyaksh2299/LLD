from typing import Dict, List
from ParkingLot.models.ParkingSpot import ParkingSpot
from ParkingLot.enums.SpotType import SpotType
from ParkingLot.models.ParkingFloor import ParkingFloor
from ParkingLot.enums.VehicleType import VehicleType

class ParkingLot:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.floors: Dict[int, ParkingFloor] = {}
        return cls._instance
    
    def add_parking_floor(self, floor: ParkingFloor):
        if floor.floor_number not in self.floors:
            self.floors[floor.floor_number] = floor

    def remove_parking_floor(self, floor: ParkingFloor):
        if floor.floor_number in self.floors:
            del self.floors[floor.floor_number]

    def find_available_spot(self, vehicle_type):
        if vehicle_type == VehicleType.CAR:
            spot_type = "COMPACT"
        elif vehicle_type == VehicleType.MOTORCYCLE:
            spot_type = "BIKE"
        elif vehicle_type == VehicleType.TRUCK:
            spot_type = "LARGE"
        else:
            raise ValueError("Invalid vehicle type")

        for floor in self.floors.values():
            spot = floor.find_available_spot(spot_type)
            if spot is not None:
                return spot

        return None

    def park_vehicle(self,vehicle):
        spot = self.find_available_spot(vehicle_type=vehicle.vehicle_type)
        if spot is None:
            raise Exception("No available parking spot for this vehicle type")
        spot.Park(vehicle)
        return spot
    
    def unpark_vehicle(self,vehicle):
        spot = self.find_available_spot(vehicle.vehicle_type)
        if spot is None:
            raise Exception("No available parking spot for this vehicle type")
        spot.Unpark(vehicle)
        return spot
