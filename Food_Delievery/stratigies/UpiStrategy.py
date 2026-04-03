from stratigies.PaymentStrategy import PaymentStrategy
class UpiStrategy(PaymentStrategy):
    def __init__(self, upi_id: str):
        self.upi_id = upi_id
    def pay(self, amount):
        print(f"Paying {amount} using UPI with ID {self.upi_id}")