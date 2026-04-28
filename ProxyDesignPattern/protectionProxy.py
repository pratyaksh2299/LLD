from abc import ABC ,abstractmethod

class Service(ABC):

    @abstractmethod
    def request(self) -> None:
        pass

class RealService(Service):

    def request(self):
        print(f"accessing sensitive data from RealService!")

class ProtectionProxy(Service):
   
    def __init__(self,role):
        self._real:RealService=None
        self.role = role

    def request(self):
        if(self.role!='admin'):
            print(f'access denied')
            return
        # lazy loading of the real service
        if (self._real is None):
            self._real = RealService()
        self._real.request()

if __name__ == '__main__':

    service :RealService = ProtectionProxy("admin")
    service.request()


    