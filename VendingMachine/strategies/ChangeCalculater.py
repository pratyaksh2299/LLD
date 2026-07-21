from abc import ABC, abstractmethod

try:
    from ..models.Coins import CoinBox
except ImportError:
    from models.Coins import CoinBox


class CoinChangeStrategy(ABC):

    @abstractmethod
    def calculate_change(self, amount: int, coin_box: CoinBox):
        pass


class GreedyChangeStrategy(CoinChangeStrategy):

    def calculate_change(self, amount: int, coin_box: CoinBox):
        if amount <= 0:
            return {}

        if coin_box.get_total_amount() < amount:
            return None

        remaining = amount
        change = {}

        for coin_type in sorted(coin_box._coins.keys(), key=lambda c: c.value, reverse=True):
            count = min(remaining // coin_type.value, coin_box._coins[coin_type])
            if count > 0:
                for _ in range(count):
                    coin_box.remove_coin(coin_type)
                change[coin_type] = count
                remaining -= count * coin_type.value

        return change if remaining == 0 else None