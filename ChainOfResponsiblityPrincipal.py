from abc import ABC,abstractmethod

# Chain of Responsibility Design Pattern
class Handler(ABC):
    @abstractmethod
    def apply_leave(self):
        pass

# Concrete Handlers
class TeamLead(Handler):
        def __init__(self):
            self.next_handler :Handler = None

        def set_next_handler(self,handler:Handler):
            self.next_handler = handler

        def apply_leave(self,days):
             if days <= 3:
                 return True
             elif self.next_handler:
                 return self.next_handler.apply_leave(days)
             else:
                 return False

class Manager(Handler):
        def __init__(self):
            self.next_handler :Handler = None

        def set_next_handler(self,handler:Handler):
            self.next_handler = handler

        def apply_leave(self,days):
             if days <= 7:
                 return True
             elif self.next_handler:
                 return self.next_handler.apply_leave(days)
             else:
                 return False

class Director(Handler):
        def __init__(self):
            self.next_handler :Handler = None

        def set_next_handler(self,handler:Handler):
            self.next_handler = handler

        def apply_leave(self,days):
             if days <= 14:
                 return True
             elif self.next_handler:
                 return self.next_handler.apply_leave(days)
             else:
                 return False

if __name__ == "__main__":
     
    team_lead :Handler =TeamLead()
    manager :Handler = Manager()
    director :Handler = Director()
    team_lead.set_next_handler(manager)
    manager.set_next_handler(director)
    print(team_lead.apply_leave(2))  # True
    print(team_lead.apply_leave(5))  # True 
    print(team_lead.apply_leave(10)) # True
    print(team_lead.apply_leave(15)) # False