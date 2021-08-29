favorite_languages = {
	'jen': 'python', 
	'sarah': 'c', 
	'edward': 'ruby', 
	'phil': 'python',
	}
for name, language in favorite_languages.items():

	print(name.title() + "'s favorite language is " + language.title())
print('- -  - --  - -- - -  -- -  --  --  -')

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(name.title() + ", you are one of my friends! Your favorite language is " +
			favorite_languages[name].title())

if 'erin' not in favorite_languages.keys(): # Looking for keys that don't exist
	print('Erin, please take the poll.')

for name in sorted(favorite_languages.keys()): # Sort the dicitonary before printing
	print(name.title() + ", thank you for taking the poll.")

print('The following languages have been mentioned:')
for language in set(favorite_languages.values()): # Identifies unique values
	print(language.title())

print('- -  - --  - -- - -  -- -  --  --  -')

to_poll = ['steve', 'john', 'edward', 'rob', 'jen']
for person in to_poll:
	if person in favorite_languages.keys():
		print('Thanks for taking the poll, ' + person.title())
	else:
		print("Please take the poll " + person.title())

print('- -  - --  - -- - -  -- -  --  --  -')

person = {'first_name': 'dylan', 'last_name':'cruz', 'city': 'Port Jeff'}
print('First Name: ' + person['first_name'].title())
print('Last Name: ' + person['last_name'].title())
print('City: ' + person['city'].title())

print('- -  - --  - -- - -  -- -  --  --  -')

user_0 = {
	'username': 'dcruz',
	'first': 'dylan',
	'last': 'cruz',
	}
for key, value in user_0.items():
	print('\nKey: ' + key)
	print('Value: ' + value)
