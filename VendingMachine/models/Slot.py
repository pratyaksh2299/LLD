from dataclasses import dataclass, field
from typing import Dict

from .Product import Product


@dataclass
class Slot:
    _code: str
    _items: Dict[Product, int] = field(default_factory=dict)
    _total_items: int = 0

    def add_product(self, product: Product):
        self._items[product] = self._items.get(product, 0) + 1
        self._total_items += 1

    def remove_product(self, product: Product):
        if self._items.get(product, 0) <= 0:
            raise Exception("Product not found in slot")

        self._items[product] -= 1
        self._total_items -= 1

        if self._items[product] == 0:
            del self._items[product]

    def get_code(self):
        return self._code

    def get_items(self):
        return self._items

    def find_product(self, item_code: str):
        for product in self._items.keys():
            if product.get_code() == item_code:
                return product
        return None

    def has_product(self, product: Product) -> bool:
        return self._items.get(product, 0) > 0
