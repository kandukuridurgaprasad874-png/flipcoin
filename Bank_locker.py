class BankLocker:
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = pin
        self.__attempts = 0
        self.__locked = False

    def access_locker(self, entered_pin):
        if self.__locked:
            print("Locker is permanently locked")
            return
        if entered_pin == self.__pin:
            print(f"Access Granted to {self.owner}'s Locker")
            self.__attempts = 0

        else:
            self.__attempts += 1
            print(f"Wrong PIN - Attempt {self.__attempts}")

            if self.__attempts >= 3:
                self.__locked = True
                print("Locker Permanently Locked")

locker = BankLocker("Durga", 1234)
locker.access_locker(1111)
locker.access_locker(2222)
locker.access_locker(3333)

print()

locker.access_locker(1234)