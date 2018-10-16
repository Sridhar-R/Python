import math

def circleprint(r):
	for i in range ((2*r)+1):
		for j in range ((2*r)+1):
			dist = math.sqrt((i-r)*(i-r)+(j-r)*(j-r))
			if (dist > r-0.5 and dist < r+0.5):
				print("*",end=" ")
			else:
				print (" ",end=" ")
		print()
r=5
circleprint(r)