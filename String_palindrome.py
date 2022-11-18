# String valid palindrome
def isPalindrome(s):
    return s == s[::-1]
s = str(input("Enter words: "))
ans = isPalindrome(s)
 
if ans:
    print("this is palindrome")
else:
    print("This is not palindrome")