filename = 'text_files/pi_million_digits.txt'
"""with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())
		"""

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''

for line in lines:
	pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))


birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday doesn't appear in the first million digits of pi.")


'''
filename2 = 'text_files/programming.txt'
with open(filename2, 'w') as file_object:
	file_object.write("I love programming!\n")
	file_object.write("I love creating new games!\n")

with open(filename2, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
'''