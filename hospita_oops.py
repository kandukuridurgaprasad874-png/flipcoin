class Patient:
    def __init__(self, name):
        self.name = name


class InPatient(Patient):
    def calculate_charges(self, days):
        charge = days * 2000
        print("In-Patient:", self.name)
        print("Total Charges:", charge)


class OutPatient(Patient):
    def calculate_charges(self):
        charge = 500
        print("Out-Patient:", self.name)
        print("Total Charges:", charge)

p1 = InPatient("Durga")
p2 = OutPatient("Prasad")

p1.calculate_charges(5)
print()
p2.calculate_charges()