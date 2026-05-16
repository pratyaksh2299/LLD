from abc import ABC,abstractmethod
from ParkingLot.Enums import VehicleType,DurationType
from datetime import datetime
from ..Stratigies.ParkingFeeStrategy import ParkingFeeStrategy
class Vehicle(ABC):
    def __init__(self,vechicle_type:VehicleType,licence_plate:str,fee_stategy:ParkingFeeStrategy):
        self._vechicle_type = vechicle_type
        self._licence_plate = licence_plate
        self._entry_time = datetime.now()
        self._fee_strategy = fee_stategy
        self._exit_time = None
    @property
    def get_vehicle_type(self):
        return self._vechicle_type
    
    @property
    def get_licence_plate(self):
        return self._licence_plate
    
    def calculate_parking_duration(self) -> float:
        current_time = datetime.now()
        self._exit_time = current_time
        duration = current_time-self._entry_time
        return max(duration.total_seconds()/3600,1)
    
    def calculate_parking_fee(self) -> float:
        parking_duration = self.calculate_parking_duration()

        return self._fee_strategy.calculate_fee(parking_duration,self._vechicle_type)
    
    def get_entry_time(self):
        return self._entry_time
    
    def get_exit_time(self):
        return self._exit_time
