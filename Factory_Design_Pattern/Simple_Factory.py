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


class Factory:

    def getburger(self, type: str) -> Burger:
        if type == 'normal':
            return Normal_Burger()
        elif type == 'standared':
            return Standared_Burger()
        elif type == 'Premium':
            return PremiumBurger()
        else:
            return None


if __name__ == '__main__':
    type = 'standared'
    factory: Factory = Factory()
    burger: Burger = factory.getburger(type)
    burger.createrBurger()
