from .Vehicle import Vehicle
class BikeVehicle(Vehicle):
    def __init__(self,vehicle_type,licence_plate,fee_strategy):
        super().__init__(vehicle_type,licence_plate,fee_strategy)