n=int(input("Enter the Number: "))
sum=0.0
for i in range(1,n+1):
	sum+=float(float(i)/(i+1))
print ("The expression 1/2+2/3+...+n/n+1 is : " ,sum)