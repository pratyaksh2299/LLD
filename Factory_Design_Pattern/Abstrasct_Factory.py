from abc import ABC, abstractmethod

# ===================== Burger =====================

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


# ===================== Garlic Bread =====================

class GrlicBread(ABC):

    @abstractmethod
    def createrGrlicBread(self):
        pass


class Normal_GrlicBread(GrlicBread):
    def createrGrlicBread(self):
        print('Normal GrlicBread')


class Standared_GrlicBread(GrlicBread):
    def createrGrlicBread(self):
        print('Standared GrlicBread')


class Premium_GrlicBread(GrlicBread):
    def createrGrlicBread(self):
        print('Premimum GrlicBread')


class NormalWheatGrlicBread(GrlicBread):
    def createrGrlicBread(self):
        print('Normal Wheat GrlicBread')


class StandaredWheatGrlicBread(GrlicBread):
    def createrGrlicBread(self):
        print('Standared Wheat GrlicBread')


class PremiumWheatGrlicBread(GrlicBread):
    def createrGrlicBread(self):
        print('Premimum Wheat GrlicBread')


# ===================== Factory =====================

class Factory(ABC):

    @abstractmethod
    def getburger(self, type: str) -> Burger:
        pass

    @abstractmethod
    def getgarlicBread(self, type: str) -> GrlicBread:
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

    def getgarlicBread(self, type: str) -> GrlicBread:
        if type == 'normal':
            return Normal_GrlicBread()
        elif type == 'standared':
            return Standared_GrlicBread()
        elif type == 'Premium':
            return Premium_GrlicBread()
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

    def getgarlicBread(self, type: str) -> GrlicBread:
        if type == 'normal':
            return NormalWheatGrlicBread()
        elif type == 'standared':
            return StandaredWheatGrlicBread()
        elif type == 'Premium':
            return PremiumWheatGrlicBread()
        else:
            return None


# ===================== Main =====================

if __name__ == '__main__':
    factory: Factory = SinghFactory()
    burger = factory.getburger('standared')
    garlic = factory.getgarlicBread('standared')
    burger.createrBurger()
    garlic.createrGrlicBread()

    factory = KinghFactory()
    burger = factory.getburger('Premium')
    garlic = factory.getgarlicBread('Premium')
    burger.createrBurger()
    garlic.createrGrlicBread()
