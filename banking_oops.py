class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print("Interest Added:", interest)


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

savings = SavingsAccount("Durga", 10000)
current = CurrentAccount("Prasad", 5000)

savings.add_interest()
savings.display_balance()

print()


current.withdraw(2000)
current.display_balance()