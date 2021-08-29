import json

filename = 'number.json'

try:
	with open(filename) as f_obj:
		number = json.load(f_obj)
except FileNotFoundError:
	number = input("Please enter your favorite number: ")
	with open(filename,'w') as f_obj:
		json.dump(number, f_obj)
else:
	print("Your favorite number is " + str(number) + "!")
