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

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type, flavors = ['vanilla',
		'chocolate', 'strawberry']):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def list_flavors(self):
		print("We have the following flavors of ice cream:")
		for flavor in self.flavors:
			print("- " + flavor.title())


ralphs = IceCreamStand("Ralphs", "Ice Cream")

ralphs.describe_restaurant()
print()
ralphs.list_flavors()
print()

frigate = IceCreamStand("The Frigate", "Ice Cream", ['Cookie Dough'])
frigate.describe_restaurant()
print()
frigate.list_flavors()

print("\n")

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

class Privilege():
	def __init__(self, privileges = ['can add post', 'can delete post',
		'can ban user']):
		self.privileges = privileges

	def show_privileges(self):
		print("The user has the following privileges:")
		for privilege in self.privileges:
			print("- " + privilege)

class Admin(User):
	def __init__(self, first_name, last_name, age, sex, location, privileges = []):
		super().__init__(first_name, last_name, age, sex, location)
		self.privileges = Privilege()

steve = Admin('steve', 'smith', 37, 'male', 'new york')
steve.describe_user()
print()
steve.privileges.show_privileges()

