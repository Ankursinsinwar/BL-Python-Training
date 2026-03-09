'''
Multilevel Inheritence
'''

class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class ElectricCar(Car):
    def charge(self):
        print("Charging electric car")

e = ElectricCar()

e.start()
e.drive()
e.charge()