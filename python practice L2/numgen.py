def NumGenerato(n):
	for i in range(n+1):
		if i%5==0 and i%7==0:
			yield (i)
n=int(input("Enter the Number:"))
values=[]
for i in NumGenerato(n):
	values.append(str(i))
print (",".join(values))
			