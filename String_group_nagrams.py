# string Group Anagrams
class Solution:
   def groupAnagrams(self, strs):
      result = {}
      for i in strs:
         x = "".join(sorted(i))
         if x in result:
            result[x].append(i)
         else:
            result[x] = [i]
      return list(result.values())
pr = []
for i in range(0,int(input("How many inser string: "))):
   m = input("Enter string: ")                           
   pr.append(m)                          
ob1 = Solution()
print(ob1.groupAnagrams(pr))