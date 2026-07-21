try:
    from .VendineMachineState import VendingMachineState
except ImportError:
    from VendineMachineState import VendingMachineState


class DispensingState(VendingMachineState):
    def __init__(self, vending_machine):
        super().__init__(vending_machine)

    def name(self):
        return "DispensingState"

    def insert_coin(self, coin):
        print("Transaction already in progress. Please wait.")
        return None

    def select_item(self, item_code):
        print("Item already selected. Please dispense first.")
        return None

    def dispense_item(self):
        if self.vending_machine._selected_item is None:
            print("No item selected.")
            return None

        balance = sum(coin.value for coin in self.vending_machine._inserted_coins)
        price = self.vending_machine._last_selected_price
        change = balance - price

        print(f"Dispensing {self.vending_machine._selected_item.get_name()}")
        if change > 0:
            change_coins = self.vending_machine.issue_change(change)
            if change_coins is None:
                print("No suitable change available.")
            else:
                print(f"Returning change: {change_coins}")

        self.vending_machine._inserted_coins.clear()
        self.vending_machine._selected_item = None
        self.vending_machine._last_selected_price = 0

        from .IdealState import IdealState
        self.vending_machine.set_state(IdealState(self.vending_machine))
        return self.vending_machine._selected_item

    def return_change(self):
        print("No pending transaction.")
        return None

    def cancel_transaction(self):
        print("No active transaction to cancel.")
        return None
