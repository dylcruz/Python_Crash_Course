'''
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")
'''

'''
print("Give me two numbers, and I'll divide them.")
print("Enter q to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero!")
	else:
		print(answer)

'''

def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding='utf-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		#print("Sorry, the file " + filename + " does not exist!")
		pass
	else:
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['text_files/alice.txt', 'text_files/sidddhartha.txt', 
	'text_files/moby_dick.txt', 'text_files/little_women.txt']
for file in filenames:
	count_words(file)