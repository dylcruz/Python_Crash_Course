class Dog():
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting is response to a command"""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""Simulate a dog rolling over is reponse to a command"""
		print(self.name.title() + " rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

print()

print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")

your_dog.sit()
your_dog.roll_over()

print()

class Car():
	"""A simple attempt to represent a car"""

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer!")

	def incrememnt_odometer(self, miles):
		if miles <= 0:
			print("You can't add negative mileage!")
		else:
			self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_odometer(20)
my_new_car.read_odometer()
my_new_car.update_odometer(38)
my_new_car.read_odometer()
my_new_car.incrememnt_odometer(-5)
my_new_car.read_odometer()
my_new_car.incrememnt_odometer(200)
my_new_car.read_odometer()

print("\n")

class Battery():
	"""A simple attempt to model a battery for an electric car"""
	def __init__(self, battery_size = 70):
		self.battery_size = battery_size

	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)

	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85
		else:
			print("The battery is already 85!")

class ElectricCar(Car):
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		super().__init__(make, model, year)
		self.battery = Battery()

my_tesla = ElectricCar('teslsa', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()



