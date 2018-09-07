arr=raw_input("Enter the no of Row , Columns : ")
dimensions=[int(a) for a in arr.split(',')]
row=dimensions[0]
col=dimensions[1]

multiarray=[[0 for j in range(col)] for i in range(row)]

for i in range(row):
	for j in range(col):
		multiarray[i][j]=i*j
print multiarray 
