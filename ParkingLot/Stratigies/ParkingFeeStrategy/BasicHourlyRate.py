from .ParkingFeeStrategy import ParkingFeeStrategy
from ...Enums import DurationType, VehicleType
class BasicHourlyRate(ParkingFeeStrategy):
    
    def calculate_fee(self, parking_duration: float, vehicle_type: VehicleType):
        try:
            Rates = {
                VehicleType.CAR: 5,
                VehicleType.BIKE: 2,    
                VehicleType.TRUCK: 10
            }
            
            if vehicle_type in Rates:
                return parking_duration * Rates[vehicle_type]
            else:
                raise ValueError("Invalid vehicle type")
        except Exception as e:
            print(f"Error calculating parking fee: {e}")
            return 0