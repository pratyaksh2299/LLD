from VendingMachine import VendingMachine
from enums.CoinEnums import CoinType
from enums.ProductEnum import ProductType
from models.Product import Product
from models.Slot import Slot



def build_machine():
    product = Product("C1", "Coke", ProductType.SOFT_DRINK, 150)
    slot = Slot("S1")
    slot.add_product(product)
    return VendingMachine([slot])


print("Scenario 1: Successful purchase")
machine = build_machine()
machine.insert_coin(CoinType.DOLLAR)
machine.insert_coin(CoinType.QUARTER)
machine.insert_coin(CoinType.QUARTER)
machine.select_item("C1")
machine.dispense_item()

print("\nScenario 2: Insufficient balance")
machine = build_machine()
machine.insert_coin(CoinType.QUARTER)
machine.select_item("C1")

print("\nScenario 3: Cancel transaction")
machine = build_machine()
machine.insert_coin(CoinType.DOLLAR)
machine.cancel_transaction()

print("\nScenario 4: Change return")
machine = build_machine()
machine.insert_coin(CoinType.DOLLAR)
machine.insert_coin(CoinType.QUARTER)
machine.insert_coin(CoinType.QUARTER)
machine.insert_coin(CoinType.QUARTER)
machine.select_item("C1")
machine.dispense_item()
