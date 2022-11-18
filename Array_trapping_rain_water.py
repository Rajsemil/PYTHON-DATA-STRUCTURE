# Trapping rain water
def rain(arr):
    ans = 0
    temp = 0
    prev = 0
    for i in range(len(arr)):
        if arr[i] > prev and temp == 0:
            prev = arr[i]
        elif arr[i] >= prev:
            ans += temp
            prev = arr[i]
            temp = 0
        else:
            if i != len(arr)-1 and arr[i] < max(arr[i+1:]):
                temp += prev - arr[i]
            else:
                ans += arr[i]
                temp = 0
                prev = arr[i]
    return ans
arr = []
m = int(input("How many inserts number in array: "))
for i in range(m-1):
    n = int(input("Enter a number: "))
    arr.append(n)
print("Trapping rain water: ",rain(arr))