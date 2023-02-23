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

class Store:

    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_product(self, new_product):
        self.inventory.append(new_product)
        return self

    def sell_product(self, id):
        product = self.inventory.pop(id -1)
        product.print_info()
        return product


    def inflation(self, percent_increase):
        for product in self.inventory:
            product.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for product in self.inventory:
            if product.category == category:
                product.update_price(percent_discount, False)


    def print_store_info(self):
        # cool little trick i learned and will probably never use it again. lol
        text = "Inventory:"
        underline = "\u0332".join(text) +"\u0332"
        print(underline)
        for product in self.inventory:
            product.print_info()


# create instances of the classes
store = Store("My store")
product1 = Product("apple", 1.50, "fruit")
product2 = Product("chips", 3.00, "snacks")
product3 = Product("shirt", 20.00, "clothing")

# add prducts to the store
store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

# test out the methods
store.print_store_info()
store.inflation(1.10)
store.set_clearance("clothing", 5.00)
product = store.sell_product(0)
print(f"Sold {product.name}")
store.print_store_info()