from typing import List
from .MenuItems import MenuItem

class Restaurant:
    def __init__(self,restaurant_id:str,name:str, location :str, menu :List[MenuItem]=None):
        self.restaurant_id = restaurant_id
        self.name = name
        self.location = location
        self.menu = menu if menu is not None else []

    def get_menu(self) -> List[MenuItem]:
        return self.menu    
    
    def get_name(self) -> str:
        return self.name

    def add_menu_item(self, menu_item: MenuItem):
        self.menu.append(menu_item)

    def remove_menu_item(self, menu_item: MenuItem):
        self.menu.remove(menu_item)
    
    def update_name(self, new_name: str):
        self.name = new_name