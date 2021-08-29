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