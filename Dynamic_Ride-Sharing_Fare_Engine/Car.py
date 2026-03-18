from Vehicle import Vehicle

class Car(Vehicle):

    rate = 1.5
    
    def calculate_fare(self,distance):
        if distance < 0:
            print("Distance can't be negative!")
            return 0
        return distance * self.rate