from collections import deque
q = deque()
for i in range(0, int(input("How many insert data do you want take: ")))
	r = int(input("Enter a number: "))
	q.append(r)
print(q)
for i in range(0, int(input("How many remove data do you want take: ")))
	s = int(input("Enter a number: "))
	q.popleft(s)
print(q)
