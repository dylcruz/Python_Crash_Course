bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1]) # Returns the last element in a list
print(bicycles[-2]) # Returns second to last and so on

print()

message = 'My first bicycle was a ' + bicycles[1].title() + '.'
print(message)

print()

motorcycles = ['hona', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati' # Changes element 0 to new data
print(motorcycles)
motorcycles.append('honda') # Adding to a list
print(motorcycles)

motorcycles.insert(0, 'bmw')
print(motorcycles)
del motorcycles[-1] # Delete last element of the list
print(motorcycles)

print()

last_owned = motorcycles.pop() # Removes last item from list into a new var
print(motorcycles)
print("The last motorcycle I owned was a " + last_owned.title() + ".")
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + '.')
print(motorcycles)

print()

too_expensive = 'ducati'
motorcycles.remove(too_expensive) # Removes by name rather than index
print(motorcycles)				  # !Removes first occurence of value!
print(too_expensive)