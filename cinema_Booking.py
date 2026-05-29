class CinemaBooking:
    def __init__(self, total_seats):
        self.__seats = [False] * total_seats

    def __allocate_seat(self):
        for index in range(len(self.__seats)):
            if not self.__seats[index]:
                self.__seats[index] = True
                return index + 1
        return None

    def book_ticket(self):
        seat_number = self.__allocate_seat()

         