from abc import ABC,abstractmethod

# strategy1

class TalkableRobot(ABC):

    @abstractmethod 
    def talk(self) -> None:
        pass

class NormalTalk(TalkableRobot):

    def talk(self) ->None:
        print('Normal talk!')

class NoTalk(TalkableRobot):
    def talk(self) ->None:
        print('No talk!')


#------------------------------------------------------------------------------------

# Strategy2

class FlyableRobot(ABC):

    @abstractmethod 
    def Fly(self) -> None:
        pass

class NormalFLy(FlyableRobot):

    def Fly(self) ->None:
        print('Normal Fly!')

class NoFly(FlyableRobot):
    def Fly(self) ->None:
        print('No Fly!')
#------------------------------------------------------------------------------------

#Strategy 3

class WalkableRobot(ABC):

    @abstractmethod
    def Walk(self) ->None:
        pass

class NormalWalk(WalkableRobot):

    def Walk(self):
        print('NOrmal Walk')

class NoWalk(WalkableRobot):

    def Walk(self):
        print('NO WALK')
#-------------------------------------------------------------------------------------
class  Robot(ABC):
    def __init__(self,talkable:TalkableRobot,walkable:WalkableRobot,flyable:FlyableRobot):
        self.talkable = talkable
        self.walkable = walkable
        self.flyable = flyable
    
    def talk(self):
        self.talkable.talk()

    def walk(self):
        self.walkable.Walk()

    def fly(self):
        self.flyable.Fly()

    def Projection(self):
        pass


class CopanionRobot(Robot):
    
    def __init__(self, talkable, walkable, flyable):
        super().__init__(talkable, walkable, flyable)
    
    def Projection(self):
        print('Projectiing worker ....................')


if __name__ == '__main__':

    robot :Robot =  CopanionRobot(NormalTalk(),NoWalk(),NormalFLy())
    robot.talk()
    robot.walk()
    robot.fly()
    robot.Projection()

    robot2 :Robot =  CopanionRobot(NoTalk(),NoWalk(),NormalFLy())
    robot2.talk()
    robot2.walk()
    robot2.fly()
    robot2.Projection()