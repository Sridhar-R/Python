class shape(object):
	def __init__(self):
		pass
	
	def area(self):
		return 0

class square(shape):
	def __init__(self,l):
		shape.__init__(self)
		shape.length=l

	def area(self):
		return self.length*self.length

inp =int(input("Enter the Length:"))	
square1=square(inp)
print ("The area of square is :", (square1.area()))