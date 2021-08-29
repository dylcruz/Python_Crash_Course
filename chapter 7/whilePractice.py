# 7-4
topping = ''
while True:
	message = "\nPlease enter a topping for your pizza!"
	message += "\nType 'quit' when your done ordering: "
	topping = input(message)
	if topping == 'quit':
		break
	print ("I will add " + topping + " to your pizza!")

# 7-5
while True:
	age = input("Please enter your age: ")
	age = int(age)
	if age < 0:
		break
	elif age < 3:
		print("Your ticket price is free")
	elif age < 12:
		print("Your ticket is $10")
	else:
		print("Your ticket is $15")

