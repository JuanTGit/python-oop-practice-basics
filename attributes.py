class Car:
	wheels = 4 # Class Attribute

	def __init__(self, make, model, color):
		self.make = make # instance attribute
		self.model = model
		self.color = color
		self.gas_level = 100 

	def drive(self, miles):
		self.gas_level -= (miles // 4)
		print(f'{self.gas_level}% Fuel Remaining')

	def gas_station(self, amount):
		if self.gas_level == 100:
			print('Tank is Full')
			return
		while self.gas_level != 100 and amount > 0:
			self.gas_level += 1
			amount -= 1
			print(f'Gas level {self.gas_level}% remaining ${amount}')
		print(f'Tank is at {self.gas_level}% Thank you for stopping at our Fuel Station!')
		if amount > 0:
			print(f'${amount} refunded')


dream_car = Car('Porsche', '911 GT3 RS', 'Red')
juans_car = Car('Volkswagen', 'Jetta', 'White')
sherleys_car = Car('Toyota', 'Corolla', 'Dark Blue')

# getattr, setattr, delattr
	# print(getattr(dream_car, 'model'))
	# setattr(dream_car, 'owner', 'Juan')
	# print(dream_car.__dict__)
	# delattr(dream_car, 'owner')
	# print(dream_car.__dict__)

class Test:

	def __init__(self, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)

my_test = Test(name="Test", age=27, hometown='Houston')

