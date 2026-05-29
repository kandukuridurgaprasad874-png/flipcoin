class Employee:

    def __init__(self, name, salary):

        # instance variables
        self.name = name

        # private variable
        self.__salary = salary


    # getter method
    def get_salary(self):
        return self.__salary


    # increment method
    def increment_salary(self, percent):

        if percent <= 20:

            increase = self.__salary * percent / 100

            self.__salary = self.__salary + increase

            print("Salary Updated")

        else:
            print("Increment limit exceeded")


    # display method
    def display(self):

        print("Employee Name :", self.name)

        print("Salary :", self.__salary)



# Object Creation
e1 = Employee("Durga", 50000)


# Display Initial Salary
print("Before Increment")
e1.display()


# Increment Salary
e1.increment_salary(10)


# Display Updated Salary
print("\nAfter Increment")
e1.display()