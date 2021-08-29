# 8-9 & 8-10
def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())

def make_great(magicians):
	for magician in magicians:
		magician = magician + " the Great"
		print(magician)

magicians = ['houdini', 'david blaine', 'chris angel']
#show_magicians(magicians)
#print()
make_great(magicians)
print()
show_magicians(magicians)

# 8-12
def order_sandwich(*toppings):
	print("\nMaking a sandwich containing the following:")
	for topping in toppings:
		print("- " + topping)

order_sandwich('ham', 'cheese')
order_sandwich('b', 'l', 't')
order_sandwich('mozz', 'pickles', 'honey mustard')

print("\n\n\n")

# 8-13
def build_profile(first, last, **user_info): # Creates empty dicitonary
	"""Builds a dicitonary containing everything we know about a user"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('dylan', 'cruz',
			   				 job='it',
			   				 gf='haley',
			   				 dog='jasper')
print(user_profile)

# 8-14
def make_car(manufacturer, model, **car_info):
	car = {}
	car['manufacturer'] = manufacturer
	car['model'] = model
	for key, value in car_info.items():
		car[key] = value
	return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)