import re

emailid= input("Enter the mailid:" )
part2 = "(\w+)@(\w+)\.(com)"
r2= re.match(part2,emailid)
print (r2.group(2))