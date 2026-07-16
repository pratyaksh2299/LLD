from abc import ABC,abstractmethod
from ParkingLot.enums.FeeCalculationType import FeeCalculationType
from ParkingLot.models.Vehicle import Vehicle
from ParkingLot.enums.VehicleType import VehicleType
from datetime import datetime, timezone
from ParkingLot.models.Ticket import Ticket
class FeeCalculate(ABC):

    @abstractmethod
    def calculate_fee(self):
        pass

class FlatRateFeeCalculate(FeeCalculate):
    def __init__(self, ticket: Ticket):
        self.ticket = ticket

    def calculate_fee(self):
        if self.ticket._vehicle.get_vehicle_type() == VehicleType.CAR:
            entry_time = self.ticket.entry_time
            exit_time = datetime.now()
            duration = exit_time - entry_time
            return duration.total_seconds() // 3600 * 20
        elif self.ticket._vehicle.get_vehicle_type() == VehicleType.MOTORCYCLE:
            entry_time = self.ticket.entry_time
            exit_time = datetime.now()
            duration = exit_time - entry_time
            return duration.total_seconds() // 3600 * 10
        elif self.ticket._vehicle.get_vehicle_type() == VehicleType.TRUCK:
            entry_time = self.ticket.entry_time
            exit_time = datetime.now()
            duration = exit_time - entry_time
            return duration.total_seconds() // 3600 * 30
        else:
            raise ValueError("Invalid vehicle type")

class HourlyRateFeeCalculate(FeeCalculate):
    def __init__(self, ticket: Ticket):
        self.ticket = ticket
        
    def calculate_fee(self):
        if self.ticket._vehicle.get_vehicle_type() == VehicleType.CAR:
            entry_time = self.ticket.entry_time
            exit_time = datetime.now()
            duration = exit_time - entry_time
            return duration.total_seconds() // 3600 * 10
        elif self.ticket._vehicle.get_vehicle_type() == VehicleType.MOTORCYCLE:
            entry_time = self.ticket.entry_time
            exit_time = datetime.now()
            duration = exit_time - entry_time
            return duration.total_seconds() // 3600 * 5
        elif self.ticket._vehicle.get_vehicle_type() == VehicleType.TRUCK:
            entry_time = self.ticket.entry_time
            exit_time = datetime.now()
            duration = exit_time - entry_time
            return duration.total_seconds() // 3600 * 15
        else:
            raise ValueError("Invalid vehicle type")
