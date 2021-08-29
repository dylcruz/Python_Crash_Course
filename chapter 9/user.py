class User():
	"""Basic class for a user profile"""
	def __init__(self, first_name, last_name, age, sex, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.sex = sex
		self.location = location
		self.login_attempts = 0

	def describe_user(self):
		print("The user's full name is " + self.first_name.title() + " " + 
			self.last_name.title() + ".")

		print("The user's age is " + str(self.age) + " and they are a " + 
			self.sex + ".")

		print("The user lives in " + self.location.title())

	def greet_user(self):
		print("This is your personalized greeting, " + self.first_name.title() + 
			" " + self.last_name.title() + ".")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

class Privilege():
	def __init__(self, privileges = ['can add post', 'can delete post',
		'can ban user']):
		self.privileges = privileges

	def show_privileges(self):
		print("The user has the following privileges:")
		for privilege in self.privileges:
			print("- " + privilege)

class Admin(User):
	def __init__(self, first_name, last_name, age, sex, location, privileges = []):
		super().__init__(first_name, last_name, age, sex, location)
		self.privileges = Privilege()