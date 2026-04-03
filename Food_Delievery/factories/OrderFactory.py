from abc import ABC,abstractmethod

from models.Cart import Cart

class OrderFactory(ABC):
    @abstractmethod
    def create_order(self, cart: Cart, restaurant, user_id: int, items, user, paymentstrategy,ordertype:str):
        pass
