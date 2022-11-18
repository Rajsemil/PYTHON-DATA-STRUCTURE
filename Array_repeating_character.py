# Find repeating character words in string
str = str(input("Enter a character words: "))
rpt = set()
for ch in str:
    if(str.count(ch)>1):
        rpt.add(ch)
print("Repeatig word: ",rpt)