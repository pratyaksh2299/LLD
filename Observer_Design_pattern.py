from abc import ABC,abstractmethod

class ISubscribe(ABC):

    @abstractmethod
    def update(self)-> None:
        pass


class Ichannel(ABC):
    
    @abstractmethod
    def Subscribe(self,subs:ISubscribe) -> None:
        pass
    @abstractmethod
    def Unsubsribe(self,subs:ISubscribe) -> None:
        pass
    @abstractmethod 
    def Notify(self) ->None:
        pass

class Channel(Ichannel):
    def __init__(self,name:str):
        self.subscribers: list[ISubscribe] = []
        self.name = name
        self.latest_title = ""

    def Subscribe(self, subs: ISubscribe) -> None:
        if subs not in self.subscribers:
            self.subscribers.append(subs)

    def Unsubsribe(self, subs: ISubscribe) -> None:
        if subs in self.subscribers:
            self.subscribers.remove(subs)

    def Notify(self) -> None:
        for sub in self.subscribers:
            sub.update()

    def uploadVideo(self,title:str) -> str:
        self.latest_title = title
        self.Notify()
        return f"Channel {self.name} uploaded: {title}"
    
    def get_video_title(self) -> str:
        return self.latest_title

class Subscriber(ISubscribe):
    def __init__(self,name:str,channel:Channel):
        self.name = name
        self.channel = channel

    def update(self) -> None:
        print(f"Subscriber {self.name} received notification from channel {self.channel.name}: New video uploaded - {self.channel.get_video_title()}")


if __name__ == "__main__":
    channel1 :Ichannel  =  Channel("TechWorld")
    subscriber1 = Subscriber("Alice", channel1)
    subscriber2 = Subscriber("Bob", channel1)
    channel1.Subscribe(subscriber1)
    channel1.Subscribe(subscriber2)
    channel1.Unsubsribe(subscriber1)            
    print(channel1.uploadVideo("New Python Features in 2024"))
   