class CartItem:
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

    def total_price(self):
        return self.quantity * self.price



n = int(input("Enter number of products: "))

cart = []
grand_total = 0

for i in range(n):
    print("\nEnter product details")
    name = input("Product Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))

    item = CartItem(name, quantity, price)
    cart.append(item)

for item in cart:
    total = item.total_price()
    print(item.product_name, "Total =", total)
    grand_total += total

print("\nGrand Total =", grand_total)