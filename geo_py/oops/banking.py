from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def fund_transfer(self):
        pass
    @abstractmethod
    def bal_enq(self):
        pass
    @abstractmethod
    def tranaction_history(self):
        pass

class G_pay(Bank):
    def fund_transfer(self):
        print("g pay fund transfer")
    def bal_enq(self):
        print("g pay balance enquiry")
    def tranaction_history(self):
        print("g pay transaction history")
    def gift_card(self):
        print("gift card")

obj=G_pay()
obj.fund_transfer()
obj.tranaction_history()
obj.gift_card()
