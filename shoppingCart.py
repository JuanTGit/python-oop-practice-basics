# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    
    def __init__(self):
        self.my_cart = {}
        self.total = 0
    
    def add_to_cart(self, item, price):
        self.my_cart[item] = price
        self.total += price

    def remove_from_cart(self, item):
        if not item in self.my_cart:
            print(f'{item} does not exist in your cart.')
            return
        else:
            self.total -= self.my_cart[item]
            self.my_cart.pop(item)
    
    def show_cart(self):
        count = 1
        if not self.my_cart:
            print('Your cart is empty!')
            return
        print('General Store')
        print('=============')
        for item, value in self.my_cart.items():
            print(f'{count}. {item}: ${value}')
            count += 1
        print('=============')
        print(f'Total: ${self.total}')
        print(f'Total Items: {count - 1}')
        print('_____________')


def run():
    cart = Cart()
    while True:
        ask = input('What would you like to do? add/remove/show/quit? ').lower()
        if ask == 'quit':
            break
        elif ask == 'add':
            while True:
                item = input('What would you like to add? ').lower()
                if item == 'quit':
                    break
                price = int(input('How much does it cost? '))
                cart.add_to_cart(item, price)

        elif ask == 'remove':
            item = input('What would you like to remove? ')
            cart.remove_from_cart(item)

        elif ask == 'show':
            cart.show_cart()

        else:
            print('Invalid response. Please try again.')

run()


cart = {
        'tea': 8,
        'coffee': 3,
        'eggs': 5,
        'chips': 2
    }

# print(cart['tea'])
# cart.pop('tea')
# print(cart)
# for i, v in cart.items():
#     print(i, v)