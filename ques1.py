list1=[]
ans=[]
finalans=[]
numb =999
temp = 0
for i in range (numb,3200):
	numb= numb+1
	list1.append(numb)

print list1

print "The list Contains ", len(list1), " numbers"

def divi(a):
	
	for i in list1:
		if (i % 7 == 0) and (i % 5 != 0):
			temp = i
			ans.append(temp)
	return ans

print divi(list1)
print len(ans)," numbers are are divisible by 7 but are not multiple of 5 between 1000 to 3200 "


	