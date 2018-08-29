import numpy as np
a = input(" Enter the limit for list : ")
x = []
for i in range(0,a):
	numb = float(input("Enter the %d th elememt: " %i ))
	x.append(numb)
print "the list is ", x

div =[]
for i in x:
	b = float(i/(i*i))
	div.append(b)
print div
y=np.sum(div)
print y	

	