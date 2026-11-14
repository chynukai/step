class Product:
    def __init__(self, name="product", price=0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
    def display_info(self):
        print('Its a', self.name)
products = [Product("apple", 20, 5),Product("orange", 30, 4),Product("banana", 15, 10),Product("pineapple", 80, 2),]
for Product in products:
    Product.display_info()
print("Total for all:", sum(i.calculate_total_price() for i in products))
