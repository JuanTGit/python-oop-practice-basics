# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    
    def __init__(self, cart=[]):
        self.cart = cart
    
    def add_to_cart(self, item):
        self.cart.append(item)

    def remove_from_cart(self, item):
        self.cart.remove(item)
    
    def show_cart(self):
        for item in self.cart:
            print(f'{item}')


buggie = Cart()

buggie.add_to_cart('Juice')
buggie.add_to_cart('Bacon')
buggie.add_to_cart('Water')
buggie.add_to_cart('Eggs')

buggie.show_cart()

buggie.remove_from_cart('Eggs')

buggie.show_cart()