unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for user in confirmed_users:
	print(user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
print(pets)

print()

responses = {}
polling_active = True

while polling_active:
	name = input("What is your name? ")
	response = input("What mountain would you like to climb some day? ")
	responses[name] = response

	repeat = input("Would you like to let another person respond (y/n)? ")
	if repeat == 'n':
		polling_active = False
print("\n---- Poll Results ----")
for name, response in responses.items():
	print(name.title() + " would like to climb Mount " + response.title())