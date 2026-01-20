from abc import ABC,abstractmethod

class Database(ABC):

    @abstractmethod
    def save(self,user:str) ->None :
        pass

class SaveTomongo(Database):
    
    def save(self,user:str) ->None:
        print(f'save user to monog ---- {user}')

class SaveToSql(Database):
    
    def save(self,user:str) ->None:
        print(f'save user to sql ---- {user}')

class UserService:
    def __init__(self,db:Database):
        self.__db = db

    def storeuser(self,user:str) -> None:
        self.__db.save(user=user)

if __name__ == '__main__':
    user1:Database = SaveTomongo()
    user2:Database = SaveToSql()

    service1=UserService(user1)
    service2=UserService(user2)
    service1.storeuser('mongo_user')
    service2.storeuser('sql_user')