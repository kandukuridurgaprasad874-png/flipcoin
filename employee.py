class Employee:
    def __init__(self, name, total_days, attended_days):
        self.name = name
        self.total_days = total_days
        self.attended_days = attended_days

    def attendance_percentage(self):
        percentage = (self.attended_days / self.total_days) * 100
        print("Employee Name:", self.name)
        print("Attendance Percentage:", percentage, "%")

        if percentage < 75:
            print("Warning: Low Attendance")
        else:
            print("Attendance is Good")



name = input("Enter Employee Name: ")
total_days = int(input("Enter Total Working Days: "))
attended_days = int(input("Enter Attended Days: "))

emp = Employee(name, total_days, attended_days)
emp.attendance_percentage()