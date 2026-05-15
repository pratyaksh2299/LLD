from abc import ABC, abstractmethod 
from math import prod

class Workshop(ABC):

    @abstractmethod
    def work(self):
        pass

class Produce(Workshop):

    def work(self):
        print("Producing...")

class Assemble(Workshop):

    def work(self):
        print("Assembling...")


class Vehicle(ABC):
    def __init__(self,workshop1:Workshop,workshop2:Workshop):
        self.workshop1 = workshop1
        self.workshop2 = workshop2  


    @abstractmethod
    def manufacture(self):
        pass    


class Car(Vehicle):
    def manufacture(self):
        self.workshop1.work()
        self.workshop2.work()
        print("Car manufactured")

class Bike(Vehicle):
    def manufacture(self):
        self.workshop1.work()
        self.workshop2.work()
        print("Bike manufactured")

if __name__ == "__main__":
    produce = Produce()
    assemble = Assemble()
    car = Car(produce,assemble)
    bike = Bike(produce,assemble)
    car.manufacture()
    bike.manufacture()
    