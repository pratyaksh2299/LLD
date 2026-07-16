from ParkingLot.strategies.FeeCalculateStretagy import FeeCalculate, FlatRateFeeCalculate, HourlyRateFeeCalculate
from ParkingLot.enums.FeeCalculationType import FeeCalculationType

class FeeCalculateContext:
    def __init__(self, fee_calculation_type: FeeCalculationType):
        self.fee_calculation_type = fee_calculation_type
        
    def  calculate_fee(self, ticket):
        if self.fee_calculation_type == FeeCalculationType.FLAT_RATE:
            fee_calculator = FlatRateFeeCalculate(ticket=ticket)
            fee_calculator.calculate_fee()
        elif self.fee_calculation_type == FeeCalculationType.HOURLY_RATE:
            fee_calculator = HourlyRateFeeCalculate(ticket=ticket)
            fee_calculator.calculate_fee()
        else:
            raise ValueError("Invalid fee calculation type")
        
        return fee_calculator.calculate_fee()
