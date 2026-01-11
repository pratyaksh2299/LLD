from abc import ABC,abstractmethod
from numbers import Number
class Product:
    def __init__(self,name:str,Price:Number):
        self.name = name
        self.Price = Price
    
class ShopingCart:
    def __init__(self):
        self.__products: list[Product] = []
    
    def add_Products(self,product:Product) ->None:
        self.__products.append(product)

    def get_Products(self) -> list[Product] :
        return self.__products
    
    def calculate_Price(self) -> Number:
        total_price:Number =0
        for p in self.__products:
            total_price+=p.Price
        return total_price

class PrintInvoice:

    def __init__(self,cart:ShopingCart):
        self.__cart =cart

    def printInvoice(self) ->None:
        total_price:Number=0.0
        for c in self.__cart.get_Products():
            print(f'name : {c.name} , price : {c.Price}')
            total_price+=c.Price
        print(f'total Price : {total_price}')

class DBPersistence(ABC):
    @abstractmethod
    def save(self, cart : ShopingCart)  -> None :
        pass

## concrete classess
class SavetoFile(DBPersistence):
    
    def save(self, cart:ShopingCart):
        print('save to file')

class SavetoMongo(DBPersistence):

    def save(self, cart:ShopingCart):
        print(f'save to mongo')
        

if __name__ == '__main__':
    cart =ShopingCart()
    product1 = Product(name='iphone',Price=23456.6)
    product2 = Product(name='ipad',Price=5678.87)
    cart.add_Products(product1)
    cart.add_Products(product2)
    invoice = PrintInvoice(cart=cart)
    invoice.printInvoice()

    db :DBPersistence  = SavetoFile()
    db.save(cart=cart)
    db :DBPersistence = SavetoMongo()
    db.save(cart=cart)