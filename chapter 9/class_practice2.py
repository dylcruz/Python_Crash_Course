class Restaurant():
	"""Basic class for a restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("The name of the restaurant is " + self.restaurant_name.title())
		print("The type of cuisine served is " + self.cuisine_type.title())

	def open_restaurant(self):
		print("The restaurant " + self.restaurant_name.title() + " is now open!")

	def set_number_served(self, num):
		self.number_served = num

	def increment_number_served(self, num):
		self.number_served += num

tb = Restaurant("Taco Bell", "Mexican")
tb.describe_restaurant()
print("The number of people served is " + str(tb.number_served))
tb.number_served = 5
print("The number of people served is " + str(tb.number_served))
tb.increment_number_served(10)
print("The number of people served is " + str(tb.number_served))

class User():
	"""Basic class for a user profile"""
	def __init__(self, first_name, last_name, age, sex, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.sex = sex
		self.location = location
		self.login_attempts = 0

	def describe_user(self):
		print("The user's full name is " + self.first_name.title() + " " + 
			self.last_name.title() + ".")

		print("The user's age is " + str(self.age) + " and they are a " + 
			self.sex + ".")

		print("The user lives in " + self.location.title())

	def greet_user(self):
		print("This is your personalized greeting, " + self.first_name.title() + 
			" " + self.last_name.title() + ".")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

print("\n")

dylan = User('dylan', 'cruz', 23, 'male', 'long island')
dylan.describe_user()
dylan.greet_user()
print("Number of login attempts: " + str(dylan.login_attempts))
dylan.increment_login_attempts()
dylan.increment_login_attempts()
dylan.increment_login_attempts()
print("Number of login attempts: " + str(dylan.login_attempts))
dylan.reset_login_attempts()
print("Number of login attempts: " + str(dylan.login_attempts))
