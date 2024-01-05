# Syntax: class ClassName(inheritance): or class ClassName: *always capitalize out class names -- pep8 guideline*

class Student:
		pass


# Creating an Instance of a class
	# variable_name = ClassName()

student_1 = Student()
student_2 = Student()

# Adding attributes to instance
	# Syntax: instance.property = value

student_1.first_name = 'Juan'
student_1.last_name = 'Tejeda'

student_2.first_name = 'Sherley'
student_2.last_name = 'Ly'

print('Student 1:', student_1.__dict__)
print('Student 2:', student_2.__dict__)

class Car:
	pass

ford = Car()
chevy = Car()
dodge = Car()

ford.make = 'Ford'
chevy.make = 'Chevrolet'
dodge.make = 'Dodge'

class Water:
	def __init__(self, name):
		self.name = name
		print(f'{self.name} Water Instance creater')
		print(f'You can now customize this instance')

	def price(self, price):
		self.price = price
		print(f'{self.name} is being sold at ${self.price} per bottle')

fiji = Water('Fiji')
dasani = Water('Dasani')

fiji.price(8)

fiji.__dict__