# 7-8
sandwich_orders = ['pastrami', 'cuban', 'pastrami', 'reuben', 'pastrami', 'blt']
finished_sandwiches = []

print("\nThe following sandwiches have been ordered: ")
for sandwich in sandwich_orders:
	print(sandwich)

print("\nFuck, we ran out of Pastrami!!! Removing those orders...")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print()

while sandwich_orders:
	current_order = sandwich_orders.pop()
	print("Making " + current_order + ' sandwich')
	finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been made: ")
for sandwich in finished_sandwiches:
	print(sandwich)

# 7-9
# Added to existing program (Pastrami)

