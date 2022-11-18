# python next permitation 
from itertools import permutations
def lexicographical_permutation(str):
   perm = sorted(''.join(chars) for chars in permutations(str))
   for x in perm:
      print(x)
s = str(input("Enter string: "))
print("You are entered: ",s)
lexicographical_permutation(s)