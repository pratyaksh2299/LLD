from dataclasses import dataclass
from numbers import Number

try:
    from ..enums.ProductEnum import ProductType
except ImportError:
    from enums.ProductEnum import ProductType


@dataclass(eq=True, frozen=True)
class Product:
    _code: str
    _name: str
    _type: ProductType
    _price: Number

    def get_code(self):
        return self._code

    def get_name(self):
        return self._name

    def get_amount(self):
        return self._price

    def get_type(self):
        return self._type


