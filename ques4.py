a = input("Enter the number between 1 and 20 : " )
b = 0

def diction():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
		print d[i]


if (a < 21):
	diction() 

else:
	print "Please Enter the number between 1 and 20 "

