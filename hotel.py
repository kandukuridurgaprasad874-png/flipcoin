class HotelRoomBooking:

    def __init__(self, hotel_name, total_rooms):

        self.hotel_name = hotel_name

        self.__available_rooms = total_rooms

    def book_room(self, rooms):

        if rooms <= self.__available_rooms:

            self.__available_rooms -= rooms

            print(rooms, "Rooms Booked")

        else:
            print("Rooms not available")

    def cancel_booking(self, rooms):

        self.__available_rooms += rooms

        print(rooms, "Rooms Cancelled")

    def display(self):

        print("Hotel Name :", self.hotel_name)

        print("Available Rooms :", self.__available_rooms)

h1 = HotelRoomBooking("Taj Hotel", 10)

print("Initial Status")
h1.display()
print("\nFirst Booking")
h1.book_room(3)
print("\nSecond Booking")
h1.book_room(2)
print("\nAfter Booking")
h1.display()
print("\nCancel Booking")
h1.cancel_booking(2)
print("\nFinal Status")
h1.display()