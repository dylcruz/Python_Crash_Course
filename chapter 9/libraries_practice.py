from random import randint

class Die():
	def __init__(self, sides = 6):
		self.sides = sides

	def roll_die(self):
		x = randint(1,self.sides)
		print(str(x))


tenSides = Die(10)
for x in range(0,10):
	tenSides.roll_die()

print()
twentySides = Die(20)
for x in range(0,10):
	twentySides.roll_die()