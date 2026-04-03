from factories.OrderFactory import OrderFactory
from models.DelieveryOrder import DeliveryOrder
from models.PickupOrder import PickupOrder
from models.Cart import Cart
from models.Order import Order
import time
class NowOrderFactory(OrderFactory):
    def __init__(self):
        order:Order=None
    def create_order(self, cart: Cart, restaurant, user_id: int, items, user, paymentstrategy,ordertype:str):
        if(ordertype == "Delivery"):
            delieveryorder = DeliveryOrder()
            delieveryorder.setDelieveryAddress("User Address") # Stub till we add to User
            order = delieveryorder
        else:
            pickuporder = PickupOrder()
            pickuporder.setRestaurantPickup(restaurant.get_name())
            order = pickuporder
        
        order.setUser(user)
        order.setRestaurant(restaurant)
        order.setItems(items)
        order.setPaymentStrategy(paymentstrategy)
        order.setScheduled_time(str(time.ctime()))
        order.setTotal(cart.get_total_price())
        return order
