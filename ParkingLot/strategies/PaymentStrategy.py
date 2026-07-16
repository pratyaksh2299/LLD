from abc import ABC, abstractmethod
from uuid import uuid4
class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

class CashPayment(PaymentStrategy):
    def __init__(self):
        self.id = str(uuid4())
    
    def process_payment(self, amount: float):
        print(f"Processing cash payment of ${amount:.2f} with ID: {self.id}")

class CardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number
        self.id = str(uuid4())
    
    def process_payment(self, amount: float):
        try:
            # Simulate card validation logic
            if len(self.card_number) != 16 or not self.card_number.isdigit():
                raise ValueError("Invalid card number. Must be 16 digits.")
            # Simulate payment processing logic
            print(f"Processing card payment of ${amount:.2f} using card {self.card_number} with ID: {self.id}")
        except ValueError as e:
            print(f"Error: {e}")

class UPIPayment(PaymentStrategy):
    def __init__(self):
        self.id = str(uuid4())

    def process_payment(self, amount: float):
        try:
            # Simulate UPI payment processing logic
            print(f"Processing UPI payment of ${amount:.2f} with ID: {self.id}")
        except Exception as e:
            print(f'Error processing UPI payment: {e}')