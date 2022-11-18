Ndef maxSubArraySum(a,size):
    max_so_far =a[0]
    curr_max = a[0]
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
    return max_so_far
a = []
for i in range(0,int(input("How many insert data: "))):
	j = int(input("Enter a number: "))
	a.append(j)

print("Inserting data: ",a)
print("Maximum contiguous sum is" , maxSubArraySum(a,len(a)))