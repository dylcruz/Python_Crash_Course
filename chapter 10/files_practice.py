filename = 'text_files/what_i_learned.txt'

with open(filename) as file_object:
	for lines in file_object:
		print(lines.strip())

'''for line in lines:
	print(line.strip())
	print(line.strip())
	print(line.strip())
'''

filename2 = 'text_files/guest.txt'

name = input("Please enter your name: ")
with open(filename2, 'w') as file_object:
	file_object.write(name + '\n')

filename2 = 'text_files/guest_book.txt'

quit = True
while(quit):
	name = input("Please enter your name: ")
	if(name == 'q'):
		quit = False
	else:
		with open(filename2, 'a') as file_object:
			file_object.write(name + '\n')

filename2 = 'text_files/why_i_like_programming.txt'

quit = True
while(quit):
	reason = input("Why do you like programming?: ")
	if(reason == 'q'):
		quit = False
	else:
		with open(filename2, 'a') as file_object:
			file_object.write(reason + '\n')
