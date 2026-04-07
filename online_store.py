class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock



Store = [
    Product("Slip and Slide", 10, 3), 
    Product("Artisan Bread", 3, 10), 
    Product("GMO Pet Hamster", 5, 5), 
    Product("Super Nintendo", 25, 5),
    Product("Universal Key", 20, 2), 
    Product("Alkaline Water", 2, 40)
]

class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.total = 0.0

    def add_product():
        pass

    def remove_product():
        pass

    def check_cart(self):
        print(self.items)

    def checkout(self):
        pass 

    


