class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


# User input
name = input("Enter Account Holder Name: ")
balance = float(input("Enter Initial Balance: "))

acc = BankAccount(name, balance)

deposit_amount = float(input("Enter Deposit Amount: "))
acc.deposit(deposit_amount)

withdraw_amount = float(input("Enter Withdraw Amount: "))
acc.withdraw(withdraw_amount)

acc.display_balance()
   