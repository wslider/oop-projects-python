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
            
            # add item to cart (first check if the item is already in the cart)

            if selected_product in self.items:
                self.items[selected_product] += quantity
            else:
                self.items[selected_product] = quantity 

            # reduce stock of item in store

            selected_product.stock -= quantity 
            
            print(f"Successfully added {quantity} of {selected_product} to your cart!")

        except ValueError:
            print("Enter a valid product number!")



    def remove_product(self, store):

        if not self.items: 
            print("\n Your Shopping Cart is Empty 🙃 Nothing to remove!")

        # cart list of items to remove
        cart_list = list(self.items.keys())

        for i, product in enumerate(cart_list, 1):
            quantity_in_cart = self.items[product]
            print(f"{i}. {product.name} (Quantity in Cart: {quantity_in_cart})")
        
        print("=" * 40)

        try:
            choice = int(input("Enter the number of the item you want to remove: "))
            if choice < 1 or choice > len(store):
                print("Please enter a valid number to select a product to remove.")
                return
            
            selected_product = store[choice - 1]

            quantity = int(input("How many {selected_product} would you like to remove? "))
            if quantity < 1 or quantity > quantity_in_cart:
                print("Please enter a valid quantity. ")
                return 
            
            # remove from cart 
            self.items[selected_product] -= quantity

                # if item quantity is zero
            
            # restock the store
            selected_product.stock += quantity 


        except ValueError: 
            return 

        
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




    

    


