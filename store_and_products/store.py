from product import Product

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