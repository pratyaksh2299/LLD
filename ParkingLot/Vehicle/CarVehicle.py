from .Vehicle import Vehicle

class CarVehicle(Vehicle):
    def __init__(self, vechicle_type, licence_plate, fee_stategy):
        super().__init__(vechicle_type, licence_plate, fee_stategy)

