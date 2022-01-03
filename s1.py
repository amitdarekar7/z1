class Father():
	def __init__(self):
		super().__init__()
		print("Father class constructor")

	def father(self):
		print("Father class method")

class Mother():
	def __init__(self):
		print("Mother class constructor")

	def mother(self):
		print("Mother class method")

class Son(Father,Mother):
	def __init__(self):
		super().__init__()
		print("Son class constructor")

	def son(self):
		print("Son class method")

s1=Son()


