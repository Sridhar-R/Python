import numpy as np
n=input("Enter the number of elements (n) :")
if n > 0:
	divi=[]
	sum=float(0)
	for i in range(1,n+1):
		b=(float(i)/(i+1))
		divi.append(b)
	print divi
	sum = np.sum(divi)
	print sum
else:
	print "Please enter the +ve integer"		