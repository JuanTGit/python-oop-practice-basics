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

class Employee:
	raise_amount = 1.05

	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary
		self.email = (first + '.' + last + '@company.org').lower()

	def full_name(self):
		return f'{self.first} {self.last}'

	def change_last_name(self, last_name):
		self.last = last_name
		self.email = (self.first + "." + self.last + '@company.org').lower()
		print(f'{self.first} {self.last} Updated. {self.email} Updated.')

	def apply_raise(self):
		self.salary = int(self.salary * self.raise_amount)
		print(f'{self.full_name()} is now making {self.salary}')

emp_1 = Employee('Juan', 'Tejeda', 100000)
emp_2 = Employee('Sherley', 'Ly', 100000)

emp_2.change_last_name('Tejeda')

# emp_1.apply_raise()

class Album:
	company = 'Dreamville Records'

	def __init__(self, title, artist, release_year, song_list=[]):
		self.title = title
		self.artist = artist
		self.release_year = release_year
		self.song_list = song_list
	
	def add_song(self, song):
		self.song_list.append(song)
		# print(f'{song.name} is playing for {song.length}')
	
	def play_album(self):
		for song in self.song_list:
			print(f'{song.name} is playing {song.length} remaining...')


class Song:

	def __init__(self, name, length, features=None):
		self.name = name
		self.length = length
		self.features = features

class Artist:

	def __init__(self, name):
		self.name = name

song1 = Song('Intro', '2:09')
song2 = Song('January 28th', '4:02')
song3 = Song('A Tale of 2 Citiez', '4:29')

cole = Artist('J. Cole')

fhd = Album('2014 Forest Hills Drive', cole, 2014)

fhd.add_song(song1)
fhd.add_song(song2)
fhd.add_song(song3)

print(fhd.artist.name)