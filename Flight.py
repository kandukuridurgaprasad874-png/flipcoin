class FlightTicket:
    def __init__(self,flight_name,total_seats):
        self.flight_name=flight_name

        self.__avaliable_seats=total_seats

    def book_ticket(self):
        if self.__avaliable_seats>0:
            self.__avaliable_seats-=1
            print("ticket Booked")
        else:
            print("No seats avaliable")

    def cancel_ticket(self):
        self.__avaliable_seats+=1
        print("ticket cancelled")
    def display(self):
        print("flight name:",self.flight_name)
        print("avaliable:",self.__avaliable_seats)

f1=FlightTicket("indigo",5)
print("initial status")
f1.display()
print("\nBook ticket")
f1.display()

print("\nbook another ticket")
f1.book_ticket()
print("\nafter booking")
f1.display()
print("\ncancel ticket")
f1.cancel_ticket()
print("\nfinal status")
f1.display

        
         