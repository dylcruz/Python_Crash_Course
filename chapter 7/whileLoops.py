current_number = 1
while (current_number <= 5):
	print(current_number)
	current_number += 1

prompt = "\nTell me a word and I will say it back to you: "
prompt += '\nEnter "quit" to end the program. '
message = ""

active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print (message)

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue					# Goes back to start of the loop
	print(current_number)