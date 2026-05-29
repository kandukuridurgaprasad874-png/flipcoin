class LoanSystem:

    def __init__(self, customer_name, loan_amount, tenure):

        self.customer_name = customer_name

        self.__loan_amount = loan_amount

        self.__tenure = tenure

        self.__emi = self.__loan_amount / self.__tenure

    
    def change_tenure(self, new_tenure):

        self.__tenure = new_tenure

        self.__emi = self.__loan_amount / self.__tenure

        print("Tenure Updated")

    def display(self):

        print("Customer Name :", self.customer_name)

        print("Loan Amount :", self.__loan_amount)

        print("Tenure :", self.__tenure)

        print("EMI :", self.__emi)


l1 = LoanSystem("Durga", 120000, 12)

print("Initial Loan Details")
l1.display()
print("\nChanging Tenure")
l1.change_tenure(24)

print("\nUpdated Loan Details")
l1.display()