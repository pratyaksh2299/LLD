from typing import List
from models.Order import Order
class OrderManager:
    _instance = None
    def __new__(cls,*args,**kwards):
        if(not cls._instance):
            cls._instance = super().__new__(cls)
            cls._instance.orders = []
        return cls._instance
    
    def __init__(self):
        pass

    def createOrder(self, order:Order):
        self.orders.append(order)

    def getOrders(self) ->List[Order]:
        return self.orders