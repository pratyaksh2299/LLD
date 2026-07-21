try:
    from .HasMoneyState import HasMoneyState
    from .VendineMachineState import VendingMachineState
except ImportError:
    from HasMoneyState import HasMoneyState
    from VendineMachineState import VendingMachineState


class IdealState(VendingMachineState):

    def name(self):
        return "IdealState"

    def insert_coin(self, coin):
        self.vending_machine._inserted_coins.append(coin)
        self.vending_machine._coin_box.insert_coin(coin)

        total_balance = self.vending_machine._coin_box.get_total_amount()
        print(f"Coin {coin.name} (${coin.value / 100:.2f}) inserted. Total balance: ${total_balance / 100:.2f}")
        self.vending_machine.set_state(HasMoneyState(self.vending_machine))

    def select_item(self, item_code):
        print("Please insert coins before selecting an item.")
        return None

    def dispense_item(self):
        print("Please insert coins and select an item before dispensing.")
        return None

    def return_change(self):
        print("No coins inserted. No change to return.")
        return None

    def cancel_transaction(self):
        print("No transaction to cancel. No coins inserted.")
        return None

       