
import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ParkingLot.models.ParkingFloor import ParkingFloor
from ParkingLot.models.ParkingLot import ParkingLot
from ParkingLot.models.ParkingSpot import BikeSpot, CompactSpot, LargeSpot
from ParkingLot.enums.SpotType import SpotType
from ParkingLot.models.Vehicle import Car
from ParkingLot.enums.VehicleType import VehicleType
from ParkingLot.services.ParkingTicketManager import ParkingTicketManager
from ParkingLot.services.CalculateFee import FeeCalculateContext
from ParkingLot.enums.FeeCalculationType import FeeCalculationType
from ParkingLot.services.ConcretPayment import ConcretePayment
from ParkingLot.enums.PaymentType import PaymentType


if __name__ == "__main__":
    parking_lot = ParkingLot()

    floor1 = ParkingFloor(floor_number=1)

    compact_spot = CompactSpot(SpotType.COMPACT)
    large_spot = LargeSpot(SpotType.LARGE)
    bike_spot = BikeSpot(SpotType.BIKE)

    floor1.add_parking_spot("COMPACT", compact_spot)
    floor1.add_parking_spot("LARGE", large_spot)
    floor1.add_parking_spot("BIKE", bike_spot)

    parking_lot.add_parking_floor(floor1)

    ticket_manager = ParkingTicketManager()

    car = Car("ABC123", VehicleType.CAR)

    spot = parking_lot.park_vehicle(car)
    ticket = ticket_manager.create_ticket(car, spot)

    print("Vehicle parked")
    print("Ticket:", ticket.get_ticket_number())

    closed_ticket = ticket_manager.close_ticket(ticket.get_ticket_number())

    fee_context = FeeCalculateContext(FeeCalculationType.HOURLY_RATE)
    amount = fee_context.calculate_fee(closed_ticket)
    
    payment = ConcretePayment(PaymentType.CASH)
    payment.pay(amount)

    parking_lot.unpark_vehicle(closed_ticket._vehicle)

    print("Vehicle unparked")
