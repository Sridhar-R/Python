import numpy as np

C = int(50)
H = int(30)
D = []
Q = []

D = raw_input('Enter a Input values: ').split(',')
print D

for i in D:
	temp=int(np.sqrt(2*C*float(i)/H))
	Q.append(temp)
print Q