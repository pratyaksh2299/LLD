import time

from factories.OrderFactory import OrderFactory
from models.Cart import Cart 
from models.Order import Order
from models.DelieveryOrder import DeliveryOrder
from models.PickupOrder import PickupOrder


class ScheduledOrderFactory(OrderFactory):
    def __init__(self, scheduled_time:str = None):
        self.scheduled_time = scheduled_time
    def create_order(self, cart: Cart, restaurant, user_id: int, items, user, paymentstrategy,ordertype:str):
        if(ordertype == "Delivery"):
            delieveryorder = DeliveryOrder()
            delieveryorder.setDelieveryAddress("User Address") # Stub
            order = delieveryorder
        else:
            pickuporder = PickupOrder()
            pickuporder.setRestaurantPickup(restaurant.get_name())
            order = pickuporder
        
        order.setUser(user)
        order.setRestaurant(restaurant)
        order.setItems(items)
        order.setPaymentStrategy(paymentstrategy)
        order.setScheduled_time(self.scheduled_time if self.scheduled_time else str(time.ctime()))
        order.setTotal(cart.get_total_price())
        return order