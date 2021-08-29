print("Please enter two numbers to be added.")
print("Enter 'q' to quit.\n")


while True:
	first_num = input("First Number: ")
	if first_num == 'q':
		break
	second_num = input("Second Number: ")
	if second_num == 'q':
		break
	try:
		result = int(first_num) + int(second_num)
	except ValueError:
		print("Please enter numbers only!")
	else:
		print(str(first_num) + " + " + str(second_num) + " is " + str(result))

file1 = 'text_files/dogs.txt'
file2 = 'text_files/cats.txt'

print("\n\n")

def read_file(filename):
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		print("The file " + filename + " was not found!!")
	else:
		print("The file " + filename + " contains:")
		print(contents)

read_file(file1)
print("\n\n")
read_file(file2)

def count_words(word, filename):
	try:
		with open(filename, encoding='utf-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		print("The file " + filename + " was not found!!")
	else:
		contents = contents.lower()
		num_words = contents.count(word)
		print("The word " + word + " appears " + str(num_words) + " times.")

file3 = 'text_files/alice.txt'

count_words('happy', file3)


