from .MenuItems import MenuItem
from .User import User
from .Restaurants import Restaurant
from stratigies.PaymentStrategy import PaymentStrategy
from abc import ABC, abstractmethod
from typing import List

class Order(ABC):
    _next_order_id = 0
    def __init__(self):
        Order._next_order_id += 1
        self.order_id = Order._next_order_id
        self.restaurant : Restaurant = None
        self.user_id : int = None
        self.user : User = None
        self.items : List[MenuItem] = []
        self.paymentstrategy : PaymentStrategy = None
        self.total=0.0
        self.scheduled_time :str = None
        

    def process_payment(self) ->bool:
        if(self.paymentstrategy):
            self.paymentstrategy.pay(self.total)
            return True
        return False
    @abstractmethod
    def getType(self) -> str:
        pass
    def setUser(self, user:User):
        self.user = user

    def getorderId(self) ->int:
        return self.order_id
    def getUser(self) ->User:
        return self.user
    
    def setRestaurant(self, restaurant:Restaurant):
        self.restaurant= restaurant
    
    def getRestaurant(self) ->Restaurant:
        return self.restaurant
    
    def setItems(self,items:List[MenuItem]):
        self.items = items

    def setScheduled_time(self, scheduled_time:str):
        self.scheduled_time = scheduled_time
        
    def getItems(self) ->List[MenuItem]:
        return self.items
    
    def setPaymentStrategy(self, paymentstrategy:PaymentStrategy):
        self.paymentstrategy = paymentstrategy

    def setTotal(self, total:float):
        self.total = total