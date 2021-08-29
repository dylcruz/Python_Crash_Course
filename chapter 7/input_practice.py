# 7-1
car = input("What kind of car would you like to rent? ")
print("Let me see if I can find you a " + car + '.')

print()

# 7-2
guests = input("How many people are in your party? ")
guests = int(guests)
if guests > 8:
	print("Sorry, you will have to wait.")
else:
	print("Your table is right this way.")

print()

# 7-3
num = input("Give me a number, I'll tell ya if it's a multiple of 10: ")
num = int(num)
if (num % 10) == 0:
	print(str(num) + ' is a multiple of 10.')
else:
	print(str(num) + ' is not a multiple of 10.')

