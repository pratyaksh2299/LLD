from abc import ABC, abstractmethod

# subsystem 1
class Restaurant(ABC):

    @abstractmethod
    def show_menu(self):
        pass

class VegetarianRestaurant(Restaurant):

    def show_menu(self):
        return "Vegetarian Menu: Salad, Grilled Vegetables, Veggie Burger"
    
class NonVegetarianRestaurant(Restaurant):

    def show_menu(self):
        return "Non-Vegetarian Menu: Chicken Curry, Beef Steak, Fish Fry"
    

class VeganRestaurant(Restaurant):

    def show_menu(self):
        return "Vegan Menu: Vegan Salad, Vegan Burger, Vegan Stir Fry"

# subsystem 2
class Hotel(ABC):

    @abstractmethod
    def get_room_details(self):
        pass

class LuxuryHotel(Hotel):

    def get_room_details(self):
        return "Luxury Room Details: King Size Bed, Balcony, City View"

class BudgetHotel(Hotel):

    def get_room_details(self):
        return "Budget Room Details: Queen Size Bed, No Balcony, Street View"
    

# Facade

class TravelFacade:
    def __init__(self):
        self._veg:Restaurant = VeganRestaurant()
        self._nonveg:Restaurant =NonVegetarianRestaurant()
        self._veg:Restaurant = VegetarianRestaurant()
        self._luxury:Hotel = LuxuryHotel()
        self._budget:Hotel = BudgetHotel()

    def get_veg_menu(self):
        return self._veg.show_menu()
    
    def get_nonveg_menu(self):
        return self._nonveg.show_menu()
    
    def get_vegan_menu(self):
        return self._veg.show_menu()
    def get_luxury_room_details(self):
        return self._luxury.get_room_details()
    def get_budget_room_details(self):
        return self._budget.get_room_details()
    
# Client code
if __name__ == "__main__":
    travel:TravelFacade = TravelFacade()
    travel.get_veg_menu()
    travel.get_nonveg_menu()
    travel.get_vegan_menu()
    travel.get_luxury_room_details()
    travel.get_budget_room_details()    