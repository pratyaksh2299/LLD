from abc import ABC, abstractmethod
from uuid import uuid4
from datetime import datetime

from ParkingLot.models.ParkingSpot import ParkingSpot
from ParkingLot.models.Vehicle import Vehicle


class Ticket(ABC):
    def __init__(self, vehicle: Vehicle, parking_Spot: ParkingSpot):
        self._vehicle = vehicle
        self._parking_spot = parking_Spot
        self._ticket_number = str(uuid4())
        self.isactive = True
        self.entry_time = datetime.now()
        self.exit_time = None

    def close_ticket(self):
        self.isactive = False
        self.exit_time = datetime.now()

    def get_details(self):
        return {
          "ticket_numer": self._ticket_number,
            "vehicle_license_plate": self._vehicle.get_license_plate(),
            "vehicle_type": self._vehicle.get_vehicle_type(),
            "parking_spot_id": self._parking_spot.id,
            "entry_time": self.entry_time,
            "exit_time": self.exit_time,
        }
    
    def get_entry_time(self):
        return self.entry_time
    
    def get_ticket_number(self):
        return self._ticket_number
