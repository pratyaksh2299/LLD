from enum import Enum


class CoinType(Enum):
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUARTER = 25
    HALF_DOLLAR = 50
    DOLLAR = 100


CoinTypes = CoinType
