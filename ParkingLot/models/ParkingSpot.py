from abc import ABC,abstractmethod
from uuid import uuid4
import uuid
from ParkingLot.enums.SpotType import SpotType
from ParkingLot.models.Vehicle import Vehicle
class ParkingSpot(ABC):

    @abstractmethod
    def isavailable(self) -> bool:
        pass

    @abstractmethod
    def isocupied(self) -> bool:
        pass

class CompactSpot(ParkingSpot):

    def __init__(self,type : SpotType):
        self.type = type
        self.id = uuid.uuid4()
        self.isocupied = False
        self.isavailable = True
    
    def Park(self,vehicle : Vehicle) -> None:
        if vehicle.vehicle_type == SpotType.COMPACT:
            if self.isavailable:
                self.isocupied = True
                self.isavailable = False
            else:
                raise Exception("Spot is not available for parking")
            
    def Unpark(self,vehicle : Vehicle) -> None:
        if vehicle.vehicle_type == SpotType.COMPACT:
            if self.isocupied:
                self.isocupied = False
                self.isavailable = True
            else:
                raise Exception("Spot is not ocupied for unparking")
            
    def isavailable(self) -> bool:
        return self.isavailable
    
    def isocupied(self) -> bool:
        return self.isocupied

class LargeSpot(ParkingSpot):
    def __init__(self,type : SpotType):
        self.type = type
        self.id = uuid.uuid4()
        self.isocupied = False
        self.isavailable = True

    def Park(self,vehicle : Vehicle) -> None:
        if vehicle.vehicle_type == SpotType.LARGE:
            if self.isavailable:
                self.isocupied = True
                self.isavailable = False
            else:
                raise Exception("Spot is not available for parking")
            

    def Unpark(self,vehicle : Vehicle) -> None:
        if vehicle.vehicle_type == SpotType.LARGE:
            if self.isocupied:
                self.isocupied = False
                self.isavailable = True
            else:
                raise Exception("Spot is not ocupied for unparking")
            
    def isavailable(self) -> bool:
        return self.isavailable
    
    def isocupied(self) -> bool:
        return self.isocupied
    

class BikeSpot(ParkingSpot):
    def __init__(self,type : SpotType):
        self.type = type
        self.id = uuid.uuid4()
        self.isocupied = False
        self.isavailable = True

    def Park(self,vehicle : Vehicle) -> None:
        if vehicle.vehicle_type == SpotType.BIKE:
            if self.isavailable:
                self.isocupied = True
                self.isavailable = False
            else:
                raise Exception("Spot is not available for parking")
            

    def Unpark(self,vehicle : Vehicle) -> None:
        if vehicle.vehicle_type == SpotType.BIKE:
            if self.isocupied:
                self.isocupied = False
                self.isavailable = True
            else:
                raise Exception("Spot is not ocupied for unparking")
            
    def isavailable(self) -> bool:
        return self.isavailable
    
    def isocupied(self) -> bool:
        return self.isocupied
