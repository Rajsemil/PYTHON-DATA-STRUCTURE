# python string Wildcard String Matching
import re
s = str(input("Enter string: "))
sbs = str(input("Enter substring: "))
temp = re.compile(sbs)
res = temp.search(s)
print("The original string is : ",s)
print("The substring match is : ",res.group(0))