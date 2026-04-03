
class  MenuItem:
    def __init__(self, menu_id: str, name: str, price: float):
        self.menu_id = menu_id
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price
    
    def get_name(self) -> str:
        return self.name
    
    def update_price(self, new_price: float):
        self.price = new_price
    
    def update_name(self, new_name: str):
        self.name = new_name

    
    
    