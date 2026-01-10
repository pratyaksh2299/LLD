from numbers import Number

class Product:
    def __init__(self, name: str, price: Number):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self._products: list[Product] = []

    def add_product(self, p: Product):
        self._products.append(p)

    def get_products(self) -> list[Product]:
        return self._products

    def calculate_price(self) -> Number:
        return sum(p.price for p in self._products)


class CartDBStorage:
    def __init__(self, cart: ShoppingCart):
        self._cart = cart

    def save_to_db(self):
        print("Cart saved to DB")


class CartInvoicePrinter:
    def __init__(self, cart: ShoppingCart):
        self._cart = cart

    def print_invoice(self):
        print("Invoice")
        for p in self._cart.get_products():
            print(f"{p.name} : {p.price}")
        print(f"Total: {self._cart.calculate_price()}")


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_product(Product("iPhone", 1016000))
    cart.add_product(Product("iPad", 36000))

    storage = CartDBStorage(cart)
    storage.save_to_db()

    printer = CartInvoicePrinter(cart)
    printer.print_invoice()
