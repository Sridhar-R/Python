class person(object):
	def getgender(self):
		return "Unknown"

class male(person):
	def getgender(self):
		return "Male"

class female(person):
	def getgender(self):
		return "Female"

amale = male()
afemale = female()
print (amale.getgender())
print (afemale.getgender())