for value in range(1,21):
	print(value)
print()

#million = [value for value in range(0,1000001)]
#for value in million:
#	print(value)
#print(min(million))
#print(max(million))
#print(sum(million))

odd = [value for value in range(1,21,2)]
for value in odd:
	print(value)
print("The first three items in the list are: " + str(odd[0:3]))
print("Three items from the middle of the list are: " + str(odd[3:6]))
print("The last three itmes of the list are: " + str(odd[7:]))

print()

mult_three = [value for value in range(3,31,3)]
for value in mult_three:
	print(value)
print()

cubed = [value ** 3 for value in range(1,11)]
for value in cubed:
	print(value)


