num= input("Enter the number : ")
sum=0
temp=num
a=len(str(num))
while temp>0:
	digit =temp%10
	sum= sum+ digit**a
	temp=temp/10

if num==sum:
	print num," is Amstrong number"
else:
	print num, "is not Amstrong number"