num = input("Enter the number :")
factorial = 1
if (num < 0):
	print ("Factorial not possible for negative number")
elif (num == 0):
	print ("Factorial is 1")
else:
	for i in range(1,num+1):
		factorial = i*factorial
	print 'The factorial of',num ,' is',factorial
