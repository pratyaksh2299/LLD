from dataclasses import dataclass, field
from numbers import Number
from typing import Dict

try:
    from ..enums.CoinEnums import CoinType
except ImportError:
    from enums.CoinEnums import CoinType


@dataclass
class CoinBox:
    _amount: Number = 0
    _coins: Dict[CoinType, int] = field(default_factory=dict)

    def insert_coin(self, coin_type: CoinType):
        self._coins[coin_type] = self._coins.get(coin_type, 0) + 1
        self._amount += coin_type.value

    def remove_coin(self, coin_type: CoinType):
        if self._coins.get(coin_type, 0) <= 0:
            raise Exception("Coin not available")

        self._coins[coin_type] -= 1
        self._amount -= coin_type.value

        if self._coins[coin_type] == 0:
            del self._coins[coin_type]

    def get_total_amount(self):
        return self._amount

    # compatibility methods
    def instertCoin(self, coin_type: CoinType):
        self.insert_coin(coin_type)

    def removeCoin(self, coin_type: CoinType):
        self.remove_coin(coin_type)

    def getTotalAmount(self):
        return self.get_total_amount()


