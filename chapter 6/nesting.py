aliens = [] # Empty list to store aliens

# Make 30 green aliens
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'

	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['points'] = 15
		alien['speed'] = 'fast'


for alien in aliens[:5]:
	print(alien)
print("...")

print("The total number of aliens is " + str(len(aliens)))

print()

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

print("You ordered a " + pizza['crust'] + 
	' crust pizza with the following toppings:')
for topping in pizza['toppings']:
	print('\t' + topping)

print()

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell']
	}
for name, languages in favorite_languages.items():
	if(len(languages) > 1):
		print(name + "'s favorite languages are: ")
		for language in languages:
			print('\t' + language)
	else:
		print(name + "'s favorite language is: ")
		print('\t' + language)
	print()

print()

users = {
	'dcruz': {
		'first': 'dylan',
		'last': 'cruz',
		'location': 'long island'
		},
	'hshon': {
		'first': 'heeyeun',
		'last': 'shon',
		'location': 'buffalo'
		},
	}
# My way	
for username, full_info in users.items():
	print(username.title() + "'s Info: ")
	for info, value in full_info.items():
		print("\t" + info.title() + ": " + value.title())
	print()

# Book way
for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']

	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())