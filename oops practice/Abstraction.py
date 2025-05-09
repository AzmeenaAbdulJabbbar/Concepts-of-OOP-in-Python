from abc import ABC, abstractmethod

class shapes(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shapes):
    def __init__(self, radius):
        self.radius = radius
    def area(self): 
        return 3.14 *self.radius * self.radius
cr = circle (5)
print("Area of circle:", cr.area())


class Device(ABC):
    @abstractmethod
    def Turn_on(self):
        pass
class laptop(Device):
    def Turn_on(self):
        print("Laptop is turned on")
class mobile(Device):
    def Turn_on(self):
        print("Mobile is turned on")
la = laptop()
mo = mobile()
la.Turn_on()    
mo.Turn_on()