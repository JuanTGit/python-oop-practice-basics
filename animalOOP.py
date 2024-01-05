class Animal:

    def __init__(self, animal_type, energy=100):
        self.animal_type = animal_type
        self.energy = energy

    def eat(self, amount):
        if self.energy == 100:
            return f'{self.animal_type.name} is full!'
        while self.energy < 100 and amount > 0:
            self.energy += 1
            amount -= 1
        if amount >= 0:
            return f'{self.animal_type.name} is at {self.energy}% energy! and has {amount} pieces of food left over..'
        return f'{self.animal_type.name} is up to {self.energy}% energy!'

    def sleep(self, amount):
        count = 0
        if self.energy == 100:
            return f'{self.animal_type.name} has {self.energy}% energy but will sleep anyways.'
        while self.energy < 100 and amount > 0:
            self.energy += 1
            amount -= 1
            count += 1
        return f'{self.animal_type.name} has slept for {count} minutes and is at {self.energy}% energy!'


    def play(self, amount):
        count = 0
        if self.energy == 0:
            return f'{self.animal_type.name} has no energy to play! Please have {self.animal_type.name} eat or sleep!'
        while self.energy > 0 and amount > 0:
            self.energy -= 1
            amount -= 1
            count += 1
        return f'{self.animal_type.name} has been playing for {count} hours! and is down to {self.energy}% energy'

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

odin = Dog('Odin', 7)
teddy = Dog('Teddy', 7)
panda = Dog('Panda', 3)


dog_odin = Animal(odin)
dog_teddy = Animal(teddy)
dog_panda = Animal(panda)

print(dog_odin.play(10))
print(dog_odin.sleep(130))
print(dog_odin.eat(20))





