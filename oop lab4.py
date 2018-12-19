class Rectangle(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
	def Area(self):
		return self.width * self.height
	def Perimeter(self):
		return(self.width + self.height) * 2
	def Print_Properties(self):
		print(self.width)
		print(self.height)
my_rectangle = Rectangle(5, 4)
print(my_rectangle.Area())
print(my_rectangle.Perimeter())
my_rectangle.Print_Properties()
class Person():
	def __init__(self, name, age, city, gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def eat(self):
		
person1 = Person("Niv", "15", "tivon", "make")
