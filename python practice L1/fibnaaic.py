nnum =int (input("Please enter the number of terms:"))

n1 = 0
nth = 0
count = 0
n2 = 1


if (count < 0):
	print("Please enter the positive number")
elif (count == 1):
	print ("Fibnnaic series upto 1st term is: ", n1)
else:
	while (count < nnum):
		print (n1, nth)
		nth = n1 + n2
		n1 = n2
		n2 = nth
		count = count + 1
		
