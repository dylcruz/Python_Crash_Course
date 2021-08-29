# immutable - Value that can't change (final in Java)
# tuple - list of immutables
dimensions = (200,50)
print("Original Dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400,100) # Overwriting new value to variable, allowed
print("Modified Dimensions:")
for dimension in dimensions:
	print(dimension)

print()

menu = ('chicken', 'steak', 'salad', 'hamburger', 'soup')
print("Original Menu:")
for item in menu:
	print(item)
# menu[1] = 'hot dog' # Doesn't work, expected
print()
menu = ('hot dog', 'steak' , 'salad', 'sushi', 'soup')
print("New Menu")
for item in menu:
	print(item)