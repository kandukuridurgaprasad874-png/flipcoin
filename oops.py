class Restaurant:
    def __init__(self, name):
        self.name = name

class Order(Restaurant):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount

    def bill(self):
        gst = self.amount * 0.05
        delivery = 30
        total = self.amount + gst + delivery

        print("Restaurant:", self.name)
        print("Food Bill:", self.amount)
        print("GST:", gst)
        print("Delivery:", delivery)
        print("Total:", total)
o1 = Order("Pizza Hub", 200)
o1.bill()
