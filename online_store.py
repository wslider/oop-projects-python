class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock



store = [
    Product("Slip and Slide", 10, 3), 
    Product("Artisan Bread", 3, 10), 
    Product("GMO Pet Hamster", 5, 5), 
    Product("Super Nintendo", 25, 5),
    Product("Universal Key", 20, 2), 
    Product("Alkaline Water", 2, 40)
]

class ShoppingCart:
    def __init__(self):
        self.items = {}  # {product: quantity}

    def display_available_products(self, store):
        print("\nAvaliable Products in Our Store: ")
        # enumerate objects in store list .. starting at 1
        print("💸" * 30) 
        for i, product in enumerate(store, 1):
            print(f"{i}: {product.name}  Price: ${product.price}  Inventory: {product.stock}")
            print("-" * 30)
        print("=" * 30)


    def add_product(self, store): 
        
        self.display_available_products(store)

        try: 
            choice = int(input("Please enter your product number: "))
            if choice < 1 or choice > len(store):
                print("Please enter a valid number from our selection of inventory!")
            
            selected_product = store[choice - 1]

            quantity = int(input(f"How many {selected_product}s would you like?"))
            if quantity < 1:
                print("Quantity must be more than 0")
                return
            if quantity > selected_product.stock:
                print("Not enough {selected_product}s in stock! Please choose a lesser ammount.")
                return
            
            

        except ValueError:
            print("Enter a valid product number!")



            # check if available  
                

        # remove from stock


        # add to cart 

            # check if already in cart 


    def remove_product(self, product, quantity):

        # show items in cart 

        # select product
        
        # remove from cart

        # add to stock

    def view_cart(self):
        pass

    def get_total(self):
        pass

    def checkout(self):
       pass


# while loop - while not checked out 
while ShoppingCart.checkout(): 
    # display options
    print("What would you like to do?")
    print("1. Add Product to Cart")
    print("2. Remove Product from Cart")
    print("3. View Cart")
    print("4. View Total")
    print("5. Checkout") 


    # user input: select action ( enter option number)

    choice = input("Enter your choice: ( 1 - 5 )")

    if choice == 1: 
        ShoppingCart.add_product()
    elif choice == 2:
        ShoppingCart.remove_product()
    elif choice == 3: 
        ShoppingCart.view_cart()
    elif choice == 4:
        ShoppingCart.get_total()
    elif choice == 5:
        ShoppingCart.checkout() 
    else:
        print("Please enter a valid choice: ")




    

    


