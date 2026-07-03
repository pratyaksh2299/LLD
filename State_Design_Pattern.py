from abc import ABC, abstractmethod

class State(ABC):

    @abstractmethod
    def handle(self, traffic_light):
        pass

class RedState(State):
    def handle(self, traffic_light):
        print("Red light - Stop!")
        traffic_light.set_state(GreenState())

class GreenState(State):
    def handle(self, traffic_light):
        print("Green light - Go!")
        traffic_light.set_state(YellowState())

class YellowState(State):
    def handle(self, traffic_light):
        print("Yellow light - Slow down!")
        traffic_light.set_state(RedState())

# Context: Path: State_Design_Pattern.py
class TrafficLight:
    def __init__(self):
        self.state = RedState()
    
    def set_state(self, state):
        self.state = state

    def handle(self):
        self.state.handle(self)

if __name__ == "__main__":
    traffic_light = TrafficLight()
    for _ in range(6):
        traffic_light.handle()
    