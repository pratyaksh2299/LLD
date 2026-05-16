
from ParkingLot.Enums import VehicleType
from ParkingLot.Vehicle import Vehicle

class ParkingSpot:
    def __init__(self, spot_type:VehicleType,spot_number):
        self._spot_type = spot_type
        self.isOccupied = False
        self._spot_id = spot_number
        self._vehicle = None
    @property
    def get_spot_type(self):
        return self._spot_type
    @property
    def get_vehicle(self):
        return self._vehicle
    @property
    def spot_id(self):
        return self._spot_id
    
    @property 
    def is_occupied(self):
        return self.isOccupied
    
    def can_park(self,vehicle:Vehicle):
        pass

    def park_vehicle(self,vehicle:Vehicle):
        if self.isOccupied:
            raise Exception("Parking spot is already occupied.")
        
        if not self.can_park(vehicle):
            raise Exception("Vehicle type is not compatible with this parking spot.")
        
        self._vehicle = vehicle
        self.isOccupied = True
        print(f"Vehicle with license plate {vehicle.get_licence_plate} parked in spot {self._spot_id}.")

    def remove_vehicle(self):
        if not self.isOccupied:
            raise Exception("Parking spot is already empty.")
        
        print(f"Vehicle with license plate {self._vehicle.get_licence_plate} removed from spot {self._spot_id}.")
        self._vehicle = None
        self.isOccupied = False


# concrete parking spot classes
class CompactParkingSpot(ParkingSpot):
    def __init__(self, spot_number):
        super().__init__(VehicleType.COMPACT, spot_number)
    
    def can_park(self,vehicle:Vehicle):
        return vehicle.get_vehicle_type in [VehicleType.COMPACT, VehicleType.BIKE]
    
class CarParkingSpot(ParkingSpot):
    def __init__(self, spot_number):
        super().__init__(VehicleType.CAR, spot_number)
    
    def can_park(self,vehicle:Vehicle):
        return vehicle.get_vehicle_type == VehicleType.CAR
    
class TruckParkingSpot(ParkingSpot):
    def __init__(self, spot_number):
        super().__init__(VehicleType.TRUCK, spot_number)
    
    def can_park(self,vehicle:Vehicle):
        return vehicle.get_vehicle_type == VehicleType.TRUCK
    
class BikeParkingSpot(ParkingSpot):
    def __init__(self, spot_number):
        super().__init__(VehicleType.BIKE, spot_number)
    
    def can_park(self,vehicle:Vehicle):
        return vehicle.get_vehicle_type == VehicleType.BIKE