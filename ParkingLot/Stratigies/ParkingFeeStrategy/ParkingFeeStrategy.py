from  abc import ABC,abstractmethod

from ParkingLot.Enums import DurationType, VehicleType

class ParkingFeeStrategy(ABC):

    @abstractmethod
    def calculate_fee(self,parking_duration,vehicle_type:VehicleType):
        pass