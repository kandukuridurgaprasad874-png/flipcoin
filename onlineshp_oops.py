# Product class
class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price


# Order class
class Order:
    def __init__(self, order_id, product):
        self.order_id = order_id
        self.product = product
        self.status = "Delivered"


# Return class
class ReturnRequest:
    def __init__(self, order):
        self.order = order
        self.return_status = "Pending"

    def process_refund(self):
        self.return_status = "Refund Processed"
        print(f"Refund of ₹{self.order.product.price} processed for Order ID {self.order.order_id}")


# Creating product
p1 = Product("Laptop", 50000)

# Creating order
o1 = Order(101, p1)

# Return request
r1 = ReturnRequest(o1)

# Display details
print("Product:", p1.product_name)
print("Order ID:", o1.order_id)
print("Order Status:", o1.status)
print("Return Status:", r1.return_status)

# Process refund
r1.process_refund()

print("Updated Return Status:", r1.return_status)