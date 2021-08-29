class Employee:
	"""Class to model an employee"""
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary

	def give_raise(self, amount=0):
		if amount:
			self.salary += amount
		else:
			self.salary += 5000
