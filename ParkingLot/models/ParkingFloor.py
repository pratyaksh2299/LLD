
from typing import Dict, List
from ParkingLot.models.ParkingSpot import ParkingSpot
from ParkingLot.enums.SpotType import SpotType

class ParkingFloor:
    def __init__(self, floor_number: int):
        self.spots :Dict[str, List] = {}
        self.floor_number = floor_number
        self.id = floor_number

    def add_parking_spot(self, spottype:str,spot):
        if spottype not in SpotType.__members__:
            raise ValueError(f"Invalid spot type: {spottype}")
        
        if spottype not in self.spots:
            self.spots[spottype] = []
        self.spots[spottype].append(spot)

    def find_available_spot(self,spotype:str) -> ParkingSpot:
        if spotype not in SpotType.__members__:
            raise ValueError(f"Invalid spot type: {spotype}")
        
        if spotype not in self.spots:
            return None
        
        for spot in self.spots[spotype]:
            if spot.isavailable:
                return spot
        return None
    
    def remove_parking_spot(self, spottype:str, spot: ParkingSpot):
        if spottype not in SpotType.__members__:
            raise ValueError(f"Invalid spot type: {spottype}")
        
        if spottype not in self.spots:
            raise ValueError(f"No spots of type {spottype} found on this floor")
        
        if spot not in self.spots[spottype]:
            raise ValueError(f"Spot not found on this floor")
        
        self.spots[spottype].remove(spot)
    
