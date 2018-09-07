sent=raw_input("Enter the Sentence :")
lcase=0
ucase=0

for i in sent:
	if (i.islower()):
		lcase = lcase+1
	elif i.isupper():
		ucase = ucase+1
print "The lower case in sentence are : ", lcase
print "The upper case in sentence are : ", ucase

