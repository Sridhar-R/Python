x = (input("Enter the string: "))
print(type(x))
y= int()
def strtoint(n):
	print (int(n))
	print (type(n))
	y=int(n)
	print (y)
	print (type(y))
	return(y)
	
print ("The '%s' is changed to number  "  %x , strtoint(x))

