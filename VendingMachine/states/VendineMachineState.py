from abc import ABC, abstractmethod


class VendingMachineState(ABC):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    @abstractmethod
    def insert_coin(self, coin):
        pass

    @abstractmethod
    def select_item(self, item_code):
        pass

    @abstractmethod
    def dispense_item(self):
        pass

    @abstractmethod
    def return_change(self):
        pass

    @abstractmethod
    def cancel_transaction(self):
        pass
