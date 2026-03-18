from Car import Car
from Bike import Bike

class Ride:

    def __init__(self, Vehicle, distance, hour_of_day ):
        self.Vehicle = Vehicle
        self.distance = distance
        self.hour_of_day = hour_of_day 


    def calculate_total_fare(self):

        fare = self.Vehicle.calculate_fare(self.distance)

        if 18 <= self.hour_of_day <= 21:
            fare = fare * 2.0
        
        if isinstance(self.Vehicle, Car) and self.distance > 20:
            discount = fare * 0.10
            fare = fare - self.distance
            
        return fare
