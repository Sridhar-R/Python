class MyError(Exception):
	"""own exception class
	Attributes:
		msg	--explanation of error
	"""
	def __init__ (self,msg):
		self.msg = msg
error =MyError("Something wrong")
