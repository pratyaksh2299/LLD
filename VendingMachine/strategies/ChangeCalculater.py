from abc import ABC , abstractmethod

class CoinChangeStrategy(ABC) :

    @abstractmethod
    def return_change(self,amount : int):
        pass

    