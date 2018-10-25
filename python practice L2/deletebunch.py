li=[]
numb=int(input("Enter the number of items: " ))
for i in range(0,numb):
	a=input("Enter the %d th element :" %i)
	li.append(a)
print ("The list is : ", li)

li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print("The final list is : ", li)