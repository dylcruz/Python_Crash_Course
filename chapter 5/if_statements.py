requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")
else:
	print("Don't hold the anchovies!")

print()

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 and age_1 >= 18)

print()

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
	print('Adding mushrooms')
if 'onions' in requested_toppings:
	print('Adding onions')
if 'pineapple' in requested_toppings:
	print('Adding pineapple')

print()

banned_users = ['andrew', 'carolina', 'david']
user  = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post on the forum.")
else:
	print(user.title() + ", you are BANNED.")

print()

age = 22
if(age < 4):
	print("The tickets are free.")
elif (age < 18):
	print("The tickets are $5")
else:
	print('The tickets are $10')

print()

age = 66
if(age < 4):
	price = 0
elif (age < 18):
	price = 5
elif (age < 65):
	price = 10
elif (age >= 65):
	price = 5
print('The price of the tickets is $' + str(price))

print()








