class HospitalRecord:

    def __init__(self, patient_name, disease):

        # private variables
        self.__patient_name = patient_name
        self.__disease = disease


    # authorized access method
    def view_record(self, role):

        if role == "Doctor" or role == "Admin":

            print("Patient Name :", self.__patient_name)

            print("Disease :", self.__disease)

        else:
            print("Access Denied")



# Object Creation
p1 = HospitalRecord("Ravi", "Fever")


# Doctor Access
print("Doctor Login")
p1.view_record("Doctor")


print("\nAdmin Login")
p1.view_record("Admin")


print("\nReceptionist Login")
p1.view_record("Receptionist")