from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
        self._serviced = False

    def service(self):
        self._serviced = True
        print("Vehicle serviced")

    def get_details(self):
        return f"Brand: {self._brand}, Model: {self._model}, Serviced: {self._serviced}"

    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        print(f"Driving a car: {self._brand} {self._model}")


class Bike(Vehicle):
    def drive(self):
        print(f"Riding a fast bike: {self._brand} {self._model}")


class Truck(Vehicle):
    def drive(self):
        print(f"Operating a heavy truck: {self._brand} {self._model}")


# Example
car = Car("Toyota", "Corolla")
car.drive()
car.service()
print(car.get_details())

bike = Bike("Yamaha", "R15")
bike.drive()
bike.service()
print(bike.get_details())

truck = Truck("Ford", "F-150")
truck.drive()
truck.service()
print(truck.get_details())
