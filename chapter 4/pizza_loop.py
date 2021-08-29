pizzas = ['hawaiin', 'suasage', 'buffalo chicken']
for pizza in pizzas:
	print("I love " + pizza + " pizza.")
print("Pizza is great.")

friend_pizzas = pizzas[:]
pizzas.append('white')
friend_pizzas.append('grandma')

print("My favorite pizzas are: ")
for pizza in pizzas:
	print(pizza)
print("My friends favorite pizzas are " + str(friend_pizzas))