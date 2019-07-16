class Person():
	def __init__(self,name = " ",age = 0):
		self.name = name
		self.age = age

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def speak(self):
		print("Hello")
	def walk(self):
		print("walking away")
phenomenal = Person("phenomenal", 22)
phenomenal.speak()
print(phenomenal.get_name(),"is ", phenomenal.get_age())
phenomenal.walk()
