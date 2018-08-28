def greatest(a,b,c,great):
	return great

a = input("Enter a:")
b = input("Enter b:")
c = input("Enter c:")

if (a>=b) and (b>=c):
	great=a
elif (b>=a) and (b>=c):
	great=b
else:
	great=c
print("greatest of 3 number is",great)
