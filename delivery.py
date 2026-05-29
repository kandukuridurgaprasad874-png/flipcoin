class DeliveryPartner:
    def deliver(self, order):
        pass


class SwiggyDelivery(DeliveryPartner):
    def deliver(self, order):
        print(f"Swiggy delivered: {order}")


class ZomatoDelivery(DeliveryPartner):
    def deliver(self, order):
        print(f"Zomato delivered: {order}")


class DunzoDelivery(DeliveryPartner):
    def deliver(self, order):
        print(f"Dunzo delivered: {order}")


def start_delivery(partner, order):
    partner.deliver(order)


s = SwiggyDelivery()
z = ZomatoDelivery()
d = DunzoDelivery()

start_delivery(s, "Pizza")
start_delivery(z, "Burger")
start_delivery(d, "Biryani")