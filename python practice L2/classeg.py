class Person:
	name="Person"
	def __init__(self,name=None):
		self.name=name
allen=Person("Allen")
print ("%s name is %s" %(Person.name,allen.name))

arul=Person()
arul.person="ARUL"
print ("%s name is %s " %(Person.name, arul.name))