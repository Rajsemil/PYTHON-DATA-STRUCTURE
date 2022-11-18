# Find all duplicate characters in string
from collections import Counter
def find_dup_char(input):
	W = Counter(input)
	for letter, count in W.items():
		if (count > 1):
			print(letter)
if __name__ == "__main__":
	s = input("Enter string: ")
	find_dup_char(s)