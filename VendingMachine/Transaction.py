from dataclasses import dataclass
from typing import List
from models.Slot import Slot
from enums.CoinEnums import CoinType
from strategies.ChangeCalculater import CoinChangeStrategy,GreedyChangeStrategy
class Transaction:

        def __init__(self,slots : List[Slot],inserted_coins : List[CoinType]):
                self._slots = slots
                self._amount = 0
                self._change_amount = 0
                self._inserted_amount = sum(coin.value for coin in inserted_coins)

        def calculate_totalamount(self):
                self._amount = 0
                for slot in self._slots:
                        for product, count in slot.get_items().items():
                                self._amount += product.get_amount() * count

                self._change_amount = self._inserted_amount - self._amount

        def changed_amount(self,change_amount):
                self._change_amount = change_amount

        def __str__(self):
                return f"Total Amount: {self._amount}, Inserted Amount: {self._inserted_amount}, Change Amount: {self._change_amount}"

        
                

        