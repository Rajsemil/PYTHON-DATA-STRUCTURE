# Insert a heap take input from user
# heapq is a python library
# heapify is used to insert a data in the list
# int is used to integer value
# iinpt is used to take input fropm user 
import heapq
h = []
for i in range(0,int(input("How many take data: "))):
    j = int(input("Enter a number: "))
    h.append(j)
heapq.heapify(h)
print(h)
