class Ride_Booking:
    def calculate_fare(self,distance):
        pass

class Bikeride(Ride_Booking):
    def calculate_fare(self, distance):
        fare=distance*10
        print(f"the rent of bikeride:{fare}")

class CabRide(Ride_Booking):
    def calculate_fare(self, distance):
        fare=distance*200
        print(f"the rent ofcabride:{fare}")

class AutoRide(Ride_Booking):
    def calculate_fare(self,distance):
        fare=distance*16
        print(f"the rent of autoride:{fare}")

def ride_car(ride, distance):
    ride.calculate_fare(distance)    
    

bike=Bikeride()
cab=CabRide()
auto=AutoRide()


ride_car(bike,6)
ride_car(cab,8)    
ride_car(auto,9)    