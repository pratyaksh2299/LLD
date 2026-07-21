try:
    from .DispensingState import DispensingState
    from .VendineMachineState import VendingMachineState
except ImportError:
    from DispensingState import DispensingState
    from VendineMachineState import VendingMachineState


class HasMoneyState(VendingMachineState):

    def name(self) -> str:
        return "HasMoneyState"

    def insert_coin(self, coin):
        self.vending_machine._inserted_coins.append(coin)
        self.vending_machine._coin_box.insert_coin(coin)

        total_balance = self.vending_machine._coin_box.get_total_amount()
        print(f"Coin {coin.name} (${coin.value / 100:.2f}) inserted. Total balance: ${total_balance / 100:.2f}")

    def select_item(self, item_code):
        for slot in self.vending_machine._slots:
            product = slot.find_product(item_code)
            if product is None:
                continue

            balance = sum(coin.value for coin in self.vending_machine._inserted_coins)
            price = product.get_amount()

            if balance < price:
                print("Insufficient balance. Please insert more coins.")
                return None

            slot.remove_product(product)
            self.vending_machine._selected_item = product
            self.vending_machine._last_selected_price = price
            self.vending_machine.set_state(DispensingState(self.vending_machine))
            print(f"Item {product.get_name()} selected.")
            return product

        print("Item not found.")
        return None

    def dispense_item(self):
        print("Please select an item first.")
        return None

    def return_change(self):
        print("No change to return yet.")
        return None

    def cancel_transaction(self):
        print("Transaction cancelled.")
        balance = sum(coin.value for coin in self.vending_machine._inserted_coins)
        if balance > 0:
            change = self.vending_machine.issue_change(balance)
            if change is None:
                print("No suitable change available.")
            else:
                print(f"Returning coins to customer: {change}")

        self.vending_machine._inserted_coins.clear()
        self.vending_machine._selected_item = None
        self.vending_machine._last_selected_price = 0
        self.vending_machine.set_state(DispensingState(self.vending_machine))
        return None

