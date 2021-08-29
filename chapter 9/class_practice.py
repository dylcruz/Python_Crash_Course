class Restaurant():
	"""Basic class for a restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("The name of the restaurant is " + self.restaurant_name.title())
		print("The type of cuisine served is " + self.cuisine_type.title())

	def open_restaurant(self):
		print("The restaurant " + self.restaurant_name.title() + " is now open!")

tb = Restaurant("Taco Bell", "Mexican")


print(tb.restaurant_name.title())
print(tb.cuisine_type.title())

print()

tb.describe_restaurant()

print()

tb.open_restaurant()

print()

wendys = Restaurant("Wendy's", "Fast Food")
wendys.describe_restaurant()

print()

tl = Restaurant("Tiger Lily", "Vegetarian")
tl.describe_restaurant()

class User():
	"""Basic class for a user profile"""
	def __init__(self, first_name, last_name, age, sex, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.sex = sex
		self.location = location

	def describe_user(self):
		print("The user's full name is " + self.first_name.title() + " " + 
			self.last_name.title() + ".")

		print("The user's age is " + str(self.age) + " and they are a " + 
			self.sex + ".")

		print("The user lives in " + self.location.title())

	def greet_user(self):
		print("This is your personalized greeting, " + self.first_name.title() + 
			" " + self.last_name.title() + ".")

print("\n")

dylan = User('dylan', 'cruz', 23, 'male', 'long island')
dylan.describe_user()
dylan.greet_user()

print()

haley = User('haley', 'shon', 20, 'female', 'buffalo')
haley.describe_user()
haley.greet_user()