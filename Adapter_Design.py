from abc import ABC, abstractmethod

class Target(ABC):

    @abstractmethod
    def Printer(self):
        pass

class Adaptee:

    def LegacyPrinter(self):
        print("This is the legacy printer.")


class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def Printer(self):
        self._adaptee.LegacyPrinter()

class Client:
    def __init__(self,target):
        self._target = target
        self._target.Printer()

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    client = Client(adapter)
