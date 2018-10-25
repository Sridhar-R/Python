def removeDupli(li):
	newli=[]
	seen = set()
	for i in li:
		if i not in seen:
			seen.add(i)
			newli.append(i)
	return newli

li=[5,18,22,55,4,5,8,25,55,22,15]
print (removeDupli(li))