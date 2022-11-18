def missingNumber(arr,n):
	expected_sum = n*(n+1)/2
	actual_sum = sum(arr)
	if __name__ == '__main':
		arr = []
		n = int(input("Enter a length of array: "))
		for i in range(n-1):
			m = int(input("Enter a umber: "))
			arr.append(m)
print("Missing Number: ",missingNumber(arr,n))