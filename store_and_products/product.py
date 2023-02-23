class Product:
    
    def __init__(self,name,price,category):
        self.name = name
        self.price = price 
        self.category = category
    
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price *= percent_change
            return self.price
        elif is_increased == False:
            self.price /= percent_change
            return self.price

    def print_info(self):
        print (f" Item: {self.name} \n Cost: ${self.price}\n Category:{self.category}")
        print ("-------------------------------------------------------")
        return self