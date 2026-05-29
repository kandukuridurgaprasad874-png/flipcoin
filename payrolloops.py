# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        return self.salary

    def display(self):
        print(f"Employee: {self.name}")
        print(f"Total Pay: {self.calculate_pay()}")


# Derived class for Manager
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_pay(self):
        return self.salary + self.bonus


# Derived class for Team Lead
class TeamLead(Employee):
    def __init__(self, name, salary, incentive):
        super().__init__(name, salary)
        self.incentive = incentive

    def calculate_pay(self):
        return self.salary + self.incentive


# Creating objects
emp1 = Employee("Ravi", 30000)
mgr1 = Manager("Suresh", 50000, 10000)
lead1 = TeamLead("Priya", 40000, 5000)

# Display payroll
emp1.display()
print("------------")
mgr1.display()
print("------------")
lead1.display()