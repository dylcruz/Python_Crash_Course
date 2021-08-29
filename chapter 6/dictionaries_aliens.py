alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'yellow'
alien_1['points'] = 10
print(alien_1)

alien_1['color'] = 'red'
alien_1['points'] = 15
print(alien_1)


print()

alien_0 = {'x_position': 0, 'y_position': 25,'speed': 'slow'}
print("Original x_position " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on it's current speed

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien
	x_increment = 3
# New x_position is old plus increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x_position is ' + str(alien_0['x_position']))

# del alien_0['speed']