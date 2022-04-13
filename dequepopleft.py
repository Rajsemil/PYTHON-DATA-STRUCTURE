from collections import deque
q = deque()
q.append(int(input("Enter a number: ")))
print(q.popleft())