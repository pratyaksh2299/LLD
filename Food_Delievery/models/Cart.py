from typing import List
from .Restaurants import Restaurant
from .MenuItems import MenuItem

class Cart:
    def __init__(self,restaurant: Restaurant, items: List[MenuItem]):
        self.restaurant = restaurant
        self.items = items

    def set_restaurant(self, restaurant: Restaurant):
        self.restaurant = restaurant
        
    def get_items(self) -> List[MenuItem]:
        return self.items
    
    def get_restaurant(self) -> Restaurant:
        return self.restaurant

    def add_item(self, menu_item: MenuItem, quantity: int = 1):
        if not self.restaurant:
            raise Exception("Restaurant not set for the cart.")

        for _ in range(quantity):
            self.items.append(menu_item)

    def remove_item(self, menu_item: MenuItem):
        self.items.remove(menu_item)    

    def  get_total_price(self) -> float:
        total_price = 0.0
        for item in self.items:
            total_price += item.get_price()    
        return total_price
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def clear_cart(self):
        self.items.clear()