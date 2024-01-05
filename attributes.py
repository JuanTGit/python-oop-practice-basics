class Car:
	wheels = 4 # Class Attribute

	def __init__(self, make, model, color):
		self.make = make # instance attribute
		self.model = model
		self.color = color
		self.gas_level = 100 


dream_car = Car('Porsche', '911 GT3 RS', 'Red')
juans_car = Car('Volkswagen', 'Jetta', 'White')
sherleys_car = Car('Toyota', 'Corolla', 'Dark Blue')

print(dream_car.gas_level)
dream_car.gas_level -= 15
print(dream_car.gas_level)

