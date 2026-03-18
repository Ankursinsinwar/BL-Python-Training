from Vehicle import Vehicle

class Bike(Vehicle):

    rate = 0.5
    
    def calculate_fare(self,distance):
        if distance < 0:
            print("Distance can't be negative!")
            return 0
        return distance * self.rate