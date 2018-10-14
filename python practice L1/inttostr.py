x = int(input("Enter the integer to be string: "))
print(type(x))
y=''
def inttostr(n):
	print (str(n))
	print (type(n))
	y=str(n)
	print (type(y))
	return (y)
print ("The %d is changed to string: "  %x , inttostr(x))

