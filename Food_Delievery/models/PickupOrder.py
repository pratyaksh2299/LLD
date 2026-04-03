from .Order import Order
class PickupOrder(Order):
    def __init__(self):
        super().__init__()
        self.restaurantpickup :str = None

    def getType(self) ->str:
        return "Pickup" 
    def setRestaurantPickup(self, restaurantpickup:str):    
        self.restaurantpickup = restaurantpickup

    def getRestaurantPickup(self) ->str:
        return self.restaurantpickup
    
