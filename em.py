class ECommerceOrder:
    def __init__(self,order_id):
        self.order_id=order_id
        self.__status="placed"
        
    def get_status(self):
        return self.__status
    
    def pack_order(self):
        if self.__status=="place":
            self.__status=="PACKED"
            print("order")
        else:
            print("packing not possible")

    def ship_order(self):
        if self.__status=="packed":
            self.__status="shipped"
            print("order shipped")
        else:
            print("shipping not possible")

    def deliver_order(self):
        if self.__status=="shipped":
            self.__status="delivered"
            print("order delivered")
        else:
            print("delivery not possible") 
    def display(self):
        print("order ID :",self.order_id)
        print("order status:",self.__status)        
