# Array in reverse order
a = [] # a = [] is a empty array
for i in range(0,int(input("How many insert data: "))):  # How many take input for empty list
  b = int(input("Enter a data: ")) # take input for insert the empty list
  a.append(b) # appebd the a = [] empty ist and b = input from the  user
print(a)
print("Reversed list is: ", a[::-1]) # Print the list in reverse  order  