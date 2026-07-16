from dataclasses import dataclass
from ..enums.ProductEnum import ProductType
from numbers import Number

@dataclass
class Product:
    _name : str
    _type : ProductType
    _price : Number

