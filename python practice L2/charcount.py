s= input()
cnt={"Digits":0, "Letters" :0}
for c in s:
	if c.isdigit():
		cnt["Digits"]+=1
	elif c.isalpha():
		cnt["Letters"]+=1
	else:
		pass
print("No of Letters : ", cnt["Letters"])
print("No of Digits are: ", cnt["Digits"])
