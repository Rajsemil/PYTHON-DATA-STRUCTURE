def search (arr, l, h, key):
    if l > h:
        return -1
    mid = (l + h) // 2
    if arr[mid] == key:
        return mid
 
    # If arr[l...mid] is sorted
    if arr[l] <= arr[mid]:
 
        # As this subarray is sorted, we can quickly
        # check if key lies in half or other half
        if key >= arr[l] and key <= arr[mid]:
            return search(arr, l, mid-1, key)
        return search(arr, mid + 1, h, key)
 
    # If arr[l..mid] is not sorted, then arr[mid... r]
    # must be sorted
    if key >= arr[mid] and key <= arr[h]:
        return search(arr, mid + 1, h, key)
    return search(arr, l, mid-1, key)
 
# Driver program
arr = []
for i in range(0,int(input("How many insert data: "))):
    j = int(input("Enter a data: "))
    arr.append(j)
key = int(input("Enter a key number: "))
i = search(arr, 0, len(arr)-1, key)
if i != -1:
    print ("Index: % d"% i)
else:
    print ("Key not found")