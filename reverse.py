a = raw_input("Enter the string : ")
def reverse(a):
	s =""
	for i in a:
		s = i + s
	return s
print reverse(a)
str1 = a
str2 = reverse(a)
print "string 1 is : " , len(str1)
print "string 2 is : ", len(str2)
if str1 == str2:
	print str1, " is Palindrome"
else:
	print str1, " is not palindrome"
