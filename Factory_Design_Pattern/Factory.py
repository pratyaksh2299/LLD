from abc import ABC, abstractmethod

class Burger(ABC):

    @abstractmethod
    def createrBurger(self) -> None:
        pass


class Normal_Burger(Burger):

    def createrBurger(self):
        print('NormalBurger')


class Standared_Burger(Burger):

    def createrBurger(self):
        print('StandaredBurger')


class PremiumBurger(Burger):

    def createrBurger(self):
        print('Premimum Burger')


class NormalWheatBurger(Burger):

    def createrBurger(self):
        print('Normal Wheat Burger')


class StandaredWheatBurger(Burger):

    def createrBurger(self):
        print('Standared Wheat Burger')


class PremiumWheatBurger(Burger):

    def createrBurger(self):
        print('Premimum Wheat Burger')


class Factory(ABC):

    @abstractmethod
    def getburger(self, type: str) -> Burger:
        pass


class SinghFactory(Factory):

    def getburger(self, type: str) -> Burger:
        if type == 'normal':
            return Normal_Burger()
        elif type == 'standared':
            return Standared_Burger()
        elif type == 'Premium':
            return PremiumBurger()
        else:
            return None


class KinghFactory(Factory):

    def getburger(self, type: str) -> Burger:
        if type == 'normal':
            return NormalWheatBurger()
        elif type == 'standared':
            return StandaredWheatBurger()
        elif type == 'Premium':
            return PremiumWheatBurger()
        else:
            return None


if __name__ == '__main__':
    type = 'standared'
    factory: Factory = SinghFactory()
    burger: Burger = factory.getburger(type)
    burger.createrBurger()

    type = 'Premium'
    factory: Factory = KinghFactory()
    burger: Burger = factory.getburger(type)
    burger.createrBurger()
