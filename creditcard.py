class CreditCard:
    def pay(self,amount):
        print(f"paid{amount} using Credit Card")

class UPI:
    def pay(self,amount):
        print(f"paid{amount} using UPI")        

class Wallet:
    def pay(self,amount):
        print(f"{amount} using Wallet")       

class Checkout:
    def make_payment(self,payment_method,amount):
        payment_method.pay(amount)

cc=CreditCard()
upi=UPI()
wallet=Wallet()
checkout=Checkout()   
checkout.make_payment(cc,500)
checkout.make_payment(upi,1000)
checkout.make_payment(wallet,200)
              