str = raw_input("Enter the String: ")
rev_str = reversed(str)

if list(str) == list(rev_str):
	print("the string is palindrome")
else:
	print ("the string is not palindrome")
