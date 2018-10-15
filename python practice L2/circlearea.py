class circle(object):
	def __init__(self, r):
		self.radius= r
	def area(self):
		return self.radius**2*3.14
inp=int(input("Enter the Radius as Input: "))
circle1= circle(inp)
print (circle1.area())