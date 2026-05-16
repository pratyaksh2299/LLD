

from ParkingLot.Enums import VehicleType
from .ParkingFeeStrategy import ParkingFeeStrategy


class PremiumRateStrategy(ParkingFeeStrategy):

    def calculate_fee(self, parking_duration: float, vehicle_type):
        try:
            Premium_rate ={
                VehicleType.CAR:100,
                VehicleType.BIKE:50,
                VehicleType.TRUCK:150
            }
            if vehicle_type in Premium_rate:
                return parking_duration * Premium_rate[vehicle_type]
            else:
                raise ValueError("Invalid vehicle type")
        except Exception as e:
            print(f"Error calculating parking fee: {e}")
            return 0