from abc import ABC, abstractmethod
from typing import List

class Light:
    def on(self):
        print('Light is on')

    def off(self):
        print('Light is off')

class Ac:
    def on(self):
        print('AC is on')

    def off(self):
        print('AC is off')

    def setTemperature(self, temp):
        print(f'Set temperature to {temp}')

class ICommand(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class LightCommand(ICommand):

    def __init__(self, light: Light):
        self.light = light
        self.prev_state = 'off'

    def execute(self):
        self.light.on()
        self.prev_state = 'on'

    def undo(self):
        if self.prev_state == 'on':
            self.light.off()
            self.prev_state = 'off'

class AcCommand(ICommand):

    def __init__(self, ac: Ac):
        self.ac = ac
        self.prev_state = 'off'

    def execute(self):
        self.ac.on()
        self.ac.setTemperature(24)
        self.prev_state = 'on'

    def undo(self):
        if self.prev_state == 'on':
            self.ac.off()
            self.prev_state = 'off'
    
    def setTemperature(self, temp):
        self.ac.setTemperature(temp)

class RemoteControl:

    def __init__(self, slots: int = 2):
        # initialize with fixed number of slots
        self.commands: List[ICommand] = [None] * slots
        self.pressedButton: List[bool] = [False] * slots

    def set_command(self, index: int, command: ICommand):
        if 0 <= index < len(self.commands):
            self.commands[index] = command
            self.pressedButton[index] = False
        else:
            print('Invalid button index')

    def press_button(self, index: int):
        if 0 <= index < len(self.commands) and self.commands[index] is not None:
            if self.pressedButton[index]:
                self.commands[index].undo()
                self.pressedButton[index] = False
            else:
                self.commands[index].execute()
                self.pressedButton[index] = True
        else:
            print('Invalid button index')


if __name__ == "__main__":
    light = Light()
    ac = Ac()

    # create commands
    ac_command = AcCommand(ac)
    light_command = LightCommand(light)

    # create remote control with 2 slots
    remote_control = RemoteControl(slots=2)
    remote_control.set_command(0, light_command)
    remote_control.set_command(1, ac_command)

    # press buttons
    remote_control.press_button(0)  # Light is on
    remote_control.press_button(1)  # AC is on, Set temperature to 24

    # undo commands
    remote_control.press_button(0)  # Light is off
    remote_control.press_button(1)  # AC is off