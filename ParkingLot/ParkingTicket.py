

from pickle import NONE
import time
from .ParkingSpot import ParkingSpot

class ParkingTicket:
    def __init__(self, Spot,vehicle):
       self._vehicle = vehicle
       self._spot = Spot
       self.entry_time = vehicle.get_entry_time()
       self.exit_time = NONE       
       self._is_paid = False
       self._fee_paid = 0.0
    
    def mark_paid(self):
        self._is_paid = True
        self._fee_paid = self._vehicle.calculate_parking_fee()
        self.exit_time = time.now()

    def get_duration_hours(self):
        if self.exit_time is not None:
            duration = self.exit_time - self.entry_time
            return duration.total_seconds() / 3600
        else:
            raise ValueError("Exit time is not set. Vehicle is still parked.")
        

    def _repr_(self):
        return f"ParkingTicket(vehicle={self._vehicle.get_licence_plate}, spot={self._spot.spot_id}, entry_time={self.entry_time}, exit_time={self.exit_time}, is_paid={self._is_paid}, fee_paid={self._fee_paid})"
    
