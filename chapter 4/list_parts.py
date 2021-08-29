players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # Prints indexes 0,1,2 | Just like range, goes to last value -1
print(players[1:4])
print(players[:4]) # Omitting first index makes it start at beginning
print(players[2:]) # Reverse for omitting last index

print()

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
print()

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My foods: " + str(my_foods))
print("Friend foods: " + str(friend_foods))

print()

