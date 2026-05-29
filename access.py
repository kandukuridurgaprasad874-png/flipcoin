
class User:
    def __init__(self, name):
        self.name = name

    def login(self):
        print(f"{self.name} logged into the system")

class Employee(User):
    def __init__(self, name, clearance_level):
        super().__init__(name)
        self.clearance_level = clearance_level

    def access_employee_area(self):
        if self.clearance_level >= 1:
            print(f"{self.name} accessed Employee Area")
        else:
            print("Access Denied")

class Manager(Employee):
    def access_manager_area(self):
        if self.clearance_level >= 2:
            print(f"{self.name} accessed Manager Area")
        else:
            print("Manager Access Denied")

class Admin(Manager):
    def access_admin_area(self):
        if self.clearance_level >= 3:
            print(f"{self.name} accessed Admin Area")
        else:
            print("Admin Access Denied")
emp = Employee("Durga", 1)
mgr = Manager("Ravi", 2)
adm = Admin("Kiran", 3)
emp.login()
emp.access_employee_area()

print()
mgr.login()
mgr.access_employee_area()
mgr.access_manager_area()

print()

adm.login()
adm.access_employee_area()
adm.access_manager_area()
adm.access_admin_area()