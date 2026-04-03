from models.Restaurants import Restaurant
from typing import List

class RestaurantManager:
    _restaurant_manager_instance = None

    def __new__(cls):
        if cls._restaurant_manager_instance is None:
            cls._restaurant_manager_instance = super(RestaurantManager, cls).__new__(cls)
            cls._restaurant_manager_instance.restaurants = []
        return cls._restaurant_manager_instance
    
    def __init__(self):
        pass

    def add_restaurant(self, restaurant: Restaurant):
        self.restaurants.append(restaurant)

    def remove_restaurant(self, restaurant: Restaurant):
        self.restaurants.remove(restaurant)
        
    def get_rastaurant_by_id(self, restaurant_id: str) -> Restaurant:
        try:
             return next(restaurant for restaurant in self.restaurants if restaurant.restaurant_id == restaurant_id)
        except StopIteration:
            return None
            
    def search_restaurant(self, name: str) -> List[Restaurant]:
        return [r for r in self.restaurants if name.lower() in r.get_name().lower()]
        
    def get_all_restaurants(self) -> List[Restaurant]:
        return self.restaurants
    
    def get_restaurants_by_location(self, location: str) -> List[Restaurant]:
        return [restaurant for restaurant in self.restaurants if restaurant.location == location]