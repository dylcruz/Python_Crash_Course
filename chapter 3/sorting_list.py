cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort() # Permanently alters order of the list
print('After sort: ' + str(cars))

cars.sort(reverse=True)
print('After reverse sort: ' + str(cars))

del cars
print()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Original list: ")
print(cars)
print("Sorted list")
print(sorted(cars)) # Doesn't alter order of this, can also use 'reverse=True'
print("Original list again")
print(cars)

del cars
print()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() # Doesn't sort, just reverses order permanently
print(cars)
print("The length of the 'cars' list is " + str(len(cars))) # Len returns length of list (int)
