import printing_functions as pf

def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
usernames = ['hanna', 'ty', 'margot']
greet_users(usernames)

print("\n")

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# print_models(unprinted_designs, completed_models)
# Passes the function a copy of the list, 'unprinted_designs' isn't modified
pf.print_models(unprinted_designs[:], completed_models)

print()

print(" - Completed Models -")
print(completed_models)
print()
print(" - 'unprinted_designs' -")
print(unprinted_designs)

print()

def make_pizza(size, *toppings): # Creates a tuple, arbitrary needs to be at end
	"""Print the list of toppings that have been requested."""
	print("\nMaking a " + size + " pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza('small', 'pepperoni')
make_pizza('large', 'mushrooms', 'green peppers', 'extra cheese')

print()

def build_profile(first, last, **user_info): # Creates empty dicitonary
	"""Builds a dicitonary containing everything we know about a user"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein',
			   				 location='princeton',
			   				 field='physics')
print(user_profile)


