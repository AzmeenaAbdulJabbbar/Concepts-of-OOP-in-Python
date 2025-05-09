#parent class
class Animal:
    def speak(self):
        print("animal is speaking")

# child class
class Dog(Animal):
    def bark (self):
         print("dog bhaunk raha hai")
         #Inheritance: Dog class inherits from Animal class
d= Dog()
d.speak()
d.bark()


class Vehicle:
    def start_engine(self):
        print("Engine started")
        # Inheritance: Vehicle class is the parent class
        # and Car class is the child class
class car (Vehicle):
    def play_music(self):
        print("Playing music")
        #Inheritance: Car class inherits from Vehicle class
my_Car = car()
my_Car.start_engine()
my_Car.play_music()