def greet_user(username):
	"""Display a simple greeting."""
	# DocString, used when generating documentation
	print("Hello, " + username.title() + "!")

greet_user('dylan')


def describe_pet(pet_name, animal_type='dog'): # Positional arguments
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('borker')
describe_pet(animal_type = 'cat', pet_name = 'meow meow') # Keyword argument

print()

def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted"""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

musician2 = get_formatted_name('kanye', 'west')
print(musician2)

print()

def build_person(first_name, last_name):
	"""Return a dictionary of information about a person"""
	person = {'first':first_name, 'last':last_name}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)

print()

while True:
	print("\nPlease tell me your name: ")
	print("(enter 'q' at any time to quit)")
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")






