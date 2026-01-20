from abc import ABC, abstractmethod
from numbers import Number

class TwoDShape(ABC):

    @abstractmethod
    def area(self) -> Number:
        pass


class ThreeDShape(ABC):

    @abstractmethod
    def area(self) -> Number:
        pass

    @abstractmethod
    def volume(self) -> Number:
        pass


class Rectangle(TwoDShape):

    def __init__(self, length: Number, width: Number):
        self.__length = length
        self.__width = width

    def area(self) -> Number:
        return self.__length * self.__width


class Cube(ThreeDShape):

    def __init__(self, side: Number):
        self.__side = side

    def area(self) -> Number:
        return 6 * (self.__side ** 2)

    def volume(self) -> Number:
        return self.__side ** 3


if __name__ == '__main__':

    threeshape : ThreeDShape = Cube(45.56)
    twod : TwoDShape = Rectangle(45.67,78.76)
    print(threeshape.volume())
    print(threeshape.area())
    print(twod.area())