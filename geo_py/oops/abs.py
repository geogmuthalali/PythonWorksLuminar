# Abstraction
from abc import ABC,abstractmethod

class Bike(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def breaks(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        pass 


class Hunter(Bike) :
    def start(self):
        print("Hunter start")
    def breaks(self):
        print("Hunter breaks")
    def accelerate(self):
        print("Hunter accelerate")

obj=Hunter()
obj.start()
obj.breaks()

                     
    

