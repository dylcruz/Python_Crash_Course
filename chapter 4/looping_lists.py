magicians = ['alice' ,'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I hope to see you perform again, " + magician.title() + ".\n")
print("Thank you to everyone for performing!")

print()

for value in range(1,5): # Excludes last number
	print(value)

print()

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2)) # Starts with 2, then adds 2 next loop
print(even_numbers)

print()

squares = [] # Empty list
for value in range (1,11):
	square = value ** 2
	squares.append(square)
print(squares)
 # These do the same thing, just remove the temp 'sqaure' var in second
squares_short = []
for value in range(1,11):
	squares_short.append(value ** 2)
print(squares_short)

print()

digits = []
for value in range(0,10): # Adds numbers 0 - 9 to digits list
	digits.append(value)
print(min(digits))
print(max(digits))
print(sum(digits))
print("Min: " + str(min(digits)) + " | Max: " + str(max(digits)) + " | Sum: " + str(sum(digits)))

print()

squares_comp = [value ** 2 for value in range(1,11)] # List creation = [expression for 'value' in 'range / list']
print(squares_comp)






