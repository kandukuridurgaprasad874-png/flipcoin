# Base class
class User:
    def __init__(self, name):
        self.name = name

    def dashboard(self):
        print(f"{self.name} accesses general dashboard")


# Admin class
class Admin(User):
    def dashboard(self):
        print(f"{self.name} can manage school records and staff")


# Teacher class
class Teacher(User):
    def dashboard(self):
        print(f"{self.name} can manage attendance and marks")


# Student class
class Student(User):
    def dashboard(self):
        print(f"{self.name} can view grades and assignments")


# Objects
admin1 = Admin("Principal")
teacher1 = Teacher("Ramesh")
student1 = Student("Durga")

# Access dashboards
admin1.dashboard()
teacher1.dashboard()
student1.dashboard()