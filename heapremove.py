# Insert a heap take input from user
# heapq is a python library
# heapify is used to insert a data in the list
# int is used to integer value
# iinpt is used to take input fropm user 
# heapppop is used to remove the data in the list
import heapq
h = []
for i in range(0,int(input("How many take data: "))):
    j = int(input("Enter a number: "))
    h.append(j)
heapq.heapify(h)
for i in range(0,int(input("How many take data: "))):
    k = int(input("Enter a number: "))
    h.append(k)
heapq.heappop(h)
print(h)