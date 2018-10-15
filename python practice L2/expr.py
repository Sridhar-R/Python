import math
c=50
h=30
answ=[]
value=[x for x in input().split(',')]
for d in value:
	answ.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print (','.join(answ))