class User:
    def __init__(self, name):
        self.name = name

    def book_ride(self, destination):
        print(f"{self.name} booked a ride to {destination}")

    def accept_ride(self, customer):
        print(f"{self.name} accepted ride request from {customer}")


# Driver who can also book rides
user1 = User("Ravi")

# Acting as customer
user1.book_ride("Hyderabad")

# Acting as driver
user1.accept_ride("Priya")