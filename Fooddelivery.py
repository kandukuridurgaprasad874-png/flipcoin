class FoodDeliveryOrder:
    def __init__(self, order_id):
        self.order_id = order_id
        
        self.__stages = [
            "Order Placed",
            "Preparing",
            "Out for Delivery",
            "Delivered"
        ]
        
        self.__current_stage = 0

    def update_status(self, new_status):
        if self.__current_stage + 1 < len(self.__stages) and \
           new_status == self.__stages[self.__current_stage + 1]:
            
            self.__current_stage += 1
            print(f"Status Updated: {new_status}")
        
        elif new_status == self.__stages[self.__current_stage]:
            print("Already in this stage.")
        
        else:
            print("Invalid status change! Cannot skip stages.")

    def show_status(self):
        print(f"Current Status: {self.__stages[self.__current_stage]}")

order1 = FoodDeliveryOrder(101)
order1.show_status()

order1.update_status("Preparing")
order1.update_status("Out for Delivery")
order1.update_statu