





from FoodApp import FoodApp
from models.User import User
from models.Cart import Cart
from stratigies.UpiStrategy import UpiStrategy

if __name__ == "__main__":
    food_app = FoodApp()
    user1 = User("U1", "John Doe", "john@example.com", "1234567890", Cart(None, []))
    restaurentList = food_app.search_restaurant("Pizza")
    if not restaurentList:
        print("Restaurant not found")   
    else:
        food_app.selectRestaurant(user1, restaurentList[0])
        print(f"Selected restaurant: {restaurentList[0].get_name()}")
        
        food_app.addToCart(user1, "Margherita Pizza", 2)
        food_app.addToCart(user1, "Pepperoni Pizza", 1)
        food_app.printuserCart(user1)
        
        order = food_app.checkoutNow(user1, "Delivery", UpiStrategy("UPI_ID_12345"))
        print(f"Order ID: {order.getorderId()}, Total: {order.total}")

        food_app.pay(order, user1)
