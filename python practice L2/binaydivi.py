answ=[]
items=[x for x in input("Enter the Binary numbers: ").split(',')]
for p in items:	
	intp = int (p,2)
	if not intp%5:
		answ.append(p)
print (','.join(answ))