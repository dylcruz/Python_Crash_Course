#requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
requested_toppings = []
if requested_toppings: # Retuns true if list contains at least 1 element
	for requested_topping in requested_toppings:
		if requested_topping == 'green peppers':
			print('Sorry, we are out of green peppers.')
		else:
			print("Adding " + requested_topping)
else:
	print("Are you sure you want a plain pizza?")
print("\nFinished making your pizza!")

print()


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 
					  'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping)
	else:
		print("Sorry, " + requested_topping + " is not available.")
print("Finished making your pizza!")


