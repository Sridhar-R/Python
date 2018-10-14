def highlen(s1,s2):
	len1=len(s1)
	len2=len(s2)
	if len1>len2:
		print (" %s has the highest length" %s1)
	elif len2>len1:
		print (" %s has the highest length" %s2)
	else:
		print ("Both have equal lenth")

wrd1=(input("Enter the first string: "))
print (type(wrd1))
wrd2=(input("Enter the second string:"))
print (type(wrd2))

highlen(wrd1,wrd2)