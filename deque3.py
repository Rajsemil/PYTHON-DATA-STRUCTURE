from collections import deque
q = deque()
for i in range(0, int(input("How many data do you want take: "))):
	q.append(input("Enter a number: "))
print(q)
