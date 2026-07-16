from abc import ABC, abstractmethod
from ParkingLot.enums.PaymentType import PaymentType
from ParkingLot.strategies.PaymentStrategy import PaymentStrategy, CashPayment, CardPayment, UPIPayment
class ConcretePayment(ABC):
    def __init__(self,PaymentType : PaymentType):
        self.paymenttype = PaymentType

    def pay(self, amount: float,):
        try:
            if self.paymenttype == PaymentType.CASH:
               CashPayment().process_payment(amount)
            elif self.paymenttype == PaymentType.CARD:
                CardPayment().process_payment(amount)
            elif self.paymenttype == PaymentType.UPI:
                UPIPayment().process_payment(amount)
            else:
                raise ValueError("Invalid payment type")
        except ValueError as e:
            print(f"Error: {e}")

