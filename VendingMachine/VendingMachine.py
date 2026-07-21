from typing import List, Optional

try:
    from .models.Coins import CoinBox
    from .models.Product import Product
    from .models.Slot import Slot
    from .states.IdealState import IdealState
    from .strategies.ChangeCalculater import GreedyChangeStrategy
except ImportError:
    from models.Coins import CoinBox
    from models.Product import Product
    from models.Slot import Slot
    from states.IdealState import IdealState
    from strategies.ChangeCalculater import GreedyChangeStrategy


class VendingMachine:
    def __init__(self, slots: Optional[List[Slot]] = None):
        self._slots: List[Slot] = slots or []
        self._inserted_coins = []
        self._selected_item: Optional[Product] = None
        self._last_selected_price = 0
        self._last_change = 0
        self._coin_box = CoinBox(0)
        self._change_strategy = GreedyChangeStrategy()
        self._state = IdealState(self)

    def set_state(self, state):
        self._state = state

    def insert_coin(self, coin):
        self._state.insert_coin(coin)

    def select_item(self, item_code):
        return self._state.select_item(item_code)

    def dispense_item(self):
        return self._state.dispense_item()

    def return_change(self):
        return self._state.return_change()

    def issue_change(self, amount):
        if amount <= 0:
            return {}

        change = self._change_strategy.calculate_change(amount, self._coin_box)
        if change is None:
            return None

        self._last_change = amount
        return change

    def cancel_transaction(self):
        return self._state.cancel_transaction()
