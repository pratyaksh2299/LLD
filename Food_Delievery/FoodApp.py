from factories.NowOrderFactory import NowOrderFactory
from factories.OrderFactory import OrderFactory
from factories.SechduledOrderFactory import ScheduledOrderFactory
from managers.RestaurantManager import RestaurantManager
from managers.OrderManger import OrderManager
from models.Restaurants import Restaurant
from models.User import User
from models.MenuItems import MenuItem
from services.NotificationService import NotificationService
from stratigies.PaymentStrategy import PaymentStrategy


class FoodApp:
    def __init__(self):
        self.initialize_restaurants()

    def initialize_restaurants(self):
        restrant1 = Restaurant("R1", "Pizza Place", "123 Main St")
        restrant2 = Restaurant("R2", "Sushi Spot", "456 Elm St")
        restrant1.add_menu_item(MenuItem("M1", "Margherita Pizza", 10.99))
        restrant1.add_menu_item(MenuItem("M2", "Pepperoni Pizza", 12.99))
        restrant2.add_menu_item(MenuItem("M3", "California Roll", 8.99))

        restrauntmanager = RestaurantManager()
        restrauntmanager.add_restaurant(restrant1)
        restrauntmanager.add_restaurant(restrant2)

    def search_restaurant(self, name: str) -> Restaurant:
        restrauntmanager = RestaurantManager()
        return restrauntmanager.search_restaurant(name)
    
    def selectRestaurant(self, user: User, restaurant: Restaurant):
        cart = user.get_cart()
        cart.set_restaurant(restaurant)

    def addToCart(self,user:User, item:str, quantity:int):
        restaurant = user.get_cart().get_restaurant()
        if not restaurant:
            print("Please select a restaurant first")
            return
        for menu_item in restaurant.get_menu():
            if menu_item.get_name() == item:
                user.get_cart().add_item(menu_item, quantity)
                print(f"Added {quantity} {item} to cart")
                return
        print(f"Item {item} not found in {restaurant.get_name()}'s menu")

    def checkout(self, user: User, order_type: str, payment_strategy: PaymentStrategy, order_factory: OrderFactory):
        cart = user.get_cart()
        if not cart.get_items():
            print("Cart is empty")
            return None
        orderedRestaurant = cart.get_restaurant()
        order = order_factory.create_order(cart, orderedRestaurant, user.get_user_id(), cart.get_items(), user, payment_strategy, order_type)
        odermanager = OrderManager()
        odermanager.createOrder(order)
        return order
    
    def checkoutNow(self, user: User, order_type: str, payment_strategy: PaymentStrategy):
       return self.checkout(user, order_type, payment_strategy, NowOrderFactory())
    
    def scheduleOrder(self, user: User, order_type: str, payment_strategy: PaymentStrategy, scheduled_time:str):
        return self.checkout(user, order_type, payment_strategy, ScheduledOrderFactory(scheduled_time=scheduled_time))
    
    def pay(self,order,user):
        ispaymentdone = order.process_payment()
        if ispaymentdone:
            notificationservice = NotificationService()
            notificationservice.notify(order)
            user.get_cart().clear_cart()
        else:
            print(f"Payment failed for order {order.getorderId()}")

    def printuserCart(self, user: User):
        cart = user.get_cart()
        print(f"Cart for user {user.get_name()}:")
        item_counts = {}
        for item in cart.get_items():
            item_counts[item] = item_counts.get(item, 0) + 1
            
        for item, quantity in item_counts.items():
            print(f"{item.get_name()} x {quantity} - ${item.get_price() * quantity}")