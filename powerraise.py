import math
def ispower(n) :
	if (n==1) :
		return True
	for x in range(2,(int)(math.sqrt(n))+1) :
		y = 2
		p = (int)(math.pow(x,y))
	
		while (p<=n and p>0):
			if (p==n):
				return True
			y=y+1
			p=math.pow(x,y)
	return False

i= int(input("Enter the number as input:"))
if (ispower(i)):
	print (" %d can be expressed as raise of power"  %(i))
else:
	print(i, "cant be expressed as raise of power")



	