prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + '!')

print()

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
	print("You are tall enough to ride!")
else:
	print("Sorry, shorty.")