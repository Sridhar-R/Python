import numpy as np
a= input("Enter the limit of list: ")
x=[]
b=[]
c=[]
for i in range (0,a):
	numb=int(input("Enter %d th integer of list: " %i))
	x.append(numb)
print "the list is :", x

for i in x:
	if i>0:
		sin=float(np.sin(i*np.pi/180)*(i*np.pi/180))
		tan=float(np.tan(1/np.sqrt(i*np.pi/180)))
		b.append(sin)
		c.append(tan)
	else:
		print " Please enter postive integer"	
	
y = [e1 + e2 for e1, e2 in zip(b,c)] 

print "the sin fun is: ", b
print "the tan fun is : ", c

print ("the value of y is : " , y) 


		
