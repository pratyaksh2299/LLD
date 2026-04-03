from .Order import Order

class DeliveryOrder(Order):
    def __init__(self):
        super().__init__()
        self.delieveryaddress :str = None

    def getType(self) ->str:
        return "Delivery"
    
    def setDelieveryAddress(self, delieveryaddress:str):    
        self.delieveryaddress = delieveryaddress

    def getDelieveryAddress(self) ->str:
        return self.delieveryaddress