def soln(heads,legs):
	ns= 'No solution!'
	for i in range(heads+1):
		j=heads-i
		if 2*i+4*j==legs:
			return i,j
	return ns,ns
heads=30
legs=90
answ=soln(heads,legs)
print (answ)