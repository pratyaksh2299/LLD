from abc import abstractmethod,ABC
from numbers import Number

class Coffee(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass
    @abstractmethod
    def get_cost(self) -> Number:
        pass

class PlainCoffee(Coffee):
    def __init__(self,name:str,cost:Number):
        self.name = name
        self.cost = cost
    def get_description(self) -> str:
        return self.name    
    def get_cost(self) -> Number:
        return self.cost
    
class CoffeeDecorator(Coffee):
    def __init__(self,coffee:Coffee):
        self.coffee = coffee

class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee=coffee)
    
    def get_description(self) -> str:
        return self.coffee.get_description() + ", Milk"
    def get_cost(self) -> Number:
        return self.coffee.get_cost() + 0.5
    
class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee=coffee)
    
    def get_description(self) -> str:
        return self.coffee.get_description() + ", Sugar"
    def get_cost(self) -> Number:
        return self.coffee.get_cost() + 0.2 
    
if __name__ == "__main__":
    mycoffee :Coffee = PlainCoffee("Espresso", 2.0)
    print(f'Description: {mycoffee.get_description()}, Cost: ${mycoffee.get_cost()}')

    mycoffee = MilkDecorator(mycoffee)
    print(f'Description: {mycoffee.get_description()}, Cost: ${mycoffee.get_cost()}')
    mycoffee = SugarDecorator(mycoffee)
    print(f'Description: {mycoffee.get_description()}, Cost: ${mycoffee.get_cost()}')
        