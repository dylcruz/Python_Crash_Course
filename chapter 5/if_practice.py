alien_color = 'red'
if alien_color == 'green':
	print("You earned 5 points!")
elif alien_color == 'yellow':
	print("You earned 10 points!")
elif alien_color == 'red':
	print("You earned 15 points!")

print()

age = 65
if age < 2:
	name = 'baby'
elif age < 4:
	name = 'toddler'
elif age < 13:
	name = 'kid'
elif age < 20:
	name = 'teenager'
elif age < 65:
	name = 'adult'
elif age >= 65:
	name = 'senior'
print("You are a " + name)

print()

favorite_fruits = ['orange', 'pineapple', 'apple']

if 'orange' in favorite_fruits:
	print('You like oranges!')
if 'banana' in favorite_fruits:
	print("You like bananas")
if 'pear' in favorite_fruits:
	print("You like pears")
if 'pineapple' in favorite_fruits:
	print("You like pineapples")
if 'apple' in favorite_fruits:
	print("You like apples")


print('\n\n')

usernames = ['admin', 'joe', 'rick', 'steve', 'jane']
#usernames = []
if usernames:
	for user in usernames:
		if user == 'admin':
			print('Hello master admin')
		else:
			print('Hello ' + user)
else:
	print("We need some users!")

print('\n')

new_users = ['mike', 'StEve', 'jaNE', 'robert']
for user in new_users:
	if user.lower() in usernames:
		print("Sorry " + user + ' that username is already in use.')
	else:
		print("Welome to the site, " + user)

