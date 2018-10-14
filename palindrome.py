str = input("Enter the String: ")
rev_str = reversed(str)

if list(str) == list(rev_str):
	print(" %s is palindrome" %str)
else:
	print (" %s is not palindrome" %str)
