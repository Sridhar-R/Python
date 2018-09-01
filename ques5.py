a = raw_input("Enter the string : ")
b= bytearray(a)
c=[]
print b

for i in b:
	if i in range(48,57):
		print i
		c.append(int(unichr(i)))
print c
			