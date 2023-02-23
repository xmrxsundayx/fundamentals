from product import Product
from store import Store

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