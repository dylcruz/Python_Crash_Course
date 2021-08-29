from survey import AnonymousSurvey

# Define a question, and make it a survey.
question = "What language did you first learn to speak?"
my_survery = AnonymousSurvey(question)

# Show the question, and store responses to the question
my_survery.show_question()
print("Enter 'q' at anytime to quit.\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survery.store_response(response)

# Show the survey results
print("\nThank you to everyone who participated in the survey!")
my_survery.show_results()