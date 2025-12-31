from abc import ABC,abstractmethod

# class AbsDemo(ABC):

#     @abstractmethod
#     def test(self):
#         pass

# class AbsImpl(AbsDemo):

#     def test(self):
#         print("Hello, test calling")

# # a = AbsDemo()
# a = AbsImpl()
# a.test()

class Account(ABC):

    balance = 0

    def checkBalance(self):
        print(f"current balance is : {self.balance}")

    @abstractmethod
    def deposite(self,amt):
        pass

    @abstractmethod
    def withdrow(self,amt):
        pass

class Saving(Account):

    def deposite(self, amt):
        self.balance = self.balance+amt
    
    def withdrow(self, amt):
        if amt > self.balance:
            print("Insufficent amount")
        else:
            self.balance-=amt

class Loan(Account):

    def deposite(self, amt):
        if amt>self.balance:
            print("u dont have any loan to repay")
        else:
            self.balance-=amt
    
    def withdrow(self, amt):
        self.balance+=amt

# s  =Saving()
# s.checkBalance()
# s.deposite(5000)
# s.deposite(3000)
# s.checkBalance()
# s.withdrow(1000)
# s.checkBalance()

s  =Loan()
s.withdrow(5000)
s.checkBalance()
s.deposite(5000)
s.checkBalance()
s.deposite(6000)