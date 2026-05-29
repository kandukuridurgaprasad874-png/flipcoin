class User:
    def __init__(self, name):
        self.name = name

    
    def buy_product(self, product):
        print(f"{self.name} bought {product}")

   
    def add_product(self, product):
        print(f"{self.name} listed {product} for sale")

    def manage_products(self):
        print(f"{self.name} is managing product listings")


# Same user acting as buyer and seller
user1 = User("Durga")

# Buyer role
user1.buy_product("Laptop")

print("------------")

# Seller role
user1.add_product("Mobile Phone")
user1.manage_products()