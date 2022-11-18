# create string with with all consective duplicates remove
n = str(input("Enter string: "))
s = ""
for chr in n:
	if s=="" or chr!=s[len(s)-1]:
		s=s+chr
print(s)