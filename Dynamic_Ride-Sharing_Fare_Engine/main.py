from Car import Car
from Bike import Bike
from Ride import Ride

def main():

    car = Car()
    bike = Bike()

    ride1 = Ride(bike,21,15)
    print("Ride 1 fare : Rs.", ride1.calculate_total_fare())
    
    ride2 = Ride(bike,21,19)
    print("Ride 2 fare : Rs.", ride2.calculate_total_fare())
    
    ride3 = Ride(car,15,15)
    print("Ride 3 fare : Rs.", ride3.calculate_total_fare())
    
    ride4 = Ride(car,21,15)
    print("Ride 4 fare : Rs.", ride4.calculate_total_fare())
    
    ride5 = Ride(car,21,19)
    print("Ride 5 fare : Rs.", ride5.calculate_total_fare())


if __name__ == "__main__":
    main()