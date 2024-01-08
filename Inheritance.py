class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (2*self.length) + (2*self.width)
    

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.hypotenuse = side * (2**(1/2))


small_sq = Square(5)

# print(small_sq.perimeter())


class Car:
    def __init__(self, color, make, model, fuel=100) -> None:
        self.color = color
        self.make = make
        self.model = model
        self.fuel = fuel

    def drive(self, amount):
        while self.fuel > 0 and amount > 0:
            self.fuel -= 1
            amount -= 1
        return f'{self.fuel}/100 remains'
    
    def fill_tank(self, amount):
        while self.fuel < 100 and amount > 0:
            self.fuel += 1
            amount -= 1
        return f'fuel level: {self.fuel}/100'
    

class Ford(Car):
    def __init__(self, color, model, fuel=100) -> None:
        super().__init__(color, 'Ford', model, fuel)