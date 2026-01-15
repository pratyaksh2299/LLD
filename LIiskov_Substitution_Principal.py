from abc import ABC,abstractmethod
from numbers import Number

class NonWithdwrableAccount(ABC):

    @abstractmethod
    def deposit(self,amount :Number) -> None :
            pass
    
class WithdrawableAccount(NonWithdwrableAccount):
      
      @abstractmethod
      def withdraw(self,amount:Number) -> None :
            pass

class FixedDepositAccount(NonWithdwrableAccount):
      
      def __init__(self):
            self.__Fixedamount = 0
      
      def deposit(self , amount : Number) -> None:
            self.__Fixedamount += amount
            print(f"total amount in fd is {self.__Fixedamount}")

class CurrentAccount(WithdrawableAccount):
    def __init__(self):
        self.__Currentamount = 0

    def deposit(self,amount:Number)  -> None:
            self.__Currentamount +=amount
            print(f"total amount in cd is {self.__Currentamount}")

    def withdraw(self,amount : Number)  -> None:
        if self.__Currentamount >= amount :
            self.__Currentamount-=amount
        print(f"remaining amount in ca is {self.__Currentamount}")

class BankClient :
    __withdrawAccount : list[WithdrawableAccount] =[]
    __NonWithdwraAccount : list[NonWithdwrableAccount] =[]

    def __init__(self,w : list[WithdrawableAccount] , Nonw : list[NonWithdwrableAccount]):
        self.__withdrawAccount=w
        self.__NonWithdwraAccount=Nonw

    def procees_transtaction(self) -> None :
        for w in self.__withdrawAccount:
            w.deposit(1000.50)
            w.withdraw(50.65)
        for w in self.__NonWithdwraAccount:
            w.deposit(1000.50)
        
if __name__ ==  '__main__':
     
     w_account : list[WithdrawableAccount] = []
     Nonw_account :list[NonWithdwrableAccount] = []
     w_account.append(CurrentAccount())
     Nonw_account.append(FixedDepositAccount())
     client = BankClient(w_account ,Nonw_account)
     client.procees_transtaction()


            
    
            