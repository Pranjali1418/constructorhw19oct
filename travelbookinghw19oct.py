# Create constructor and objects of TravelBoking class

class TravelBooking:
    def __init__(self, destination, ticket_price ,stay_days):
        print(f"TravelBooking constructor is running for {destination}")
        self.destination = destination
        self.ticket_price = ticket_price
        self.stay_days = stay_days

travel1 = TravelBooking("Mumbai", 1500 , 5)
travel2 = TravelBooking("Delhi", 2200 , 11)

print(travel2.stay_days)

travel2.stay_days = 9

print(travel2.stay_days)
print(travel1.destination)