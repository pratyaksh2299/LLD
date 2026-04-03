from stratigies.PaymentStrategy import PaymentStrategy
class CreditCardStrategy(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card: {self.card_number}")