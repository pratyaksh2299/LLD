from typing import List
from .Cart import Cart
class User:
    def __init__(self, user_id: str, name: str, email: str, phone_number: str, cart:Cart):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.cart = cart

    def update_email(self, new_email: str):
        self.email = new_email  

    def update_phone_number(self, new_phone_number: str):
        self.phone_number = new_phone_number
    
    def get_cart(self) -> Cart:
        return self.cart
    
    def get_user_id(self) -> str:
        return self.user_id
    
    def get_name(self) -> str:
        return self.name
