a = [] # empt array
for i in range(0,int(input("How many insert data in array: "))):
	m = int(input("Enter a number: "))
	a.append(m)
print("Largest number is: ",min(a)) # min is used to minimum number