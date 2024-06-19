from collections import Counter
test_str = input("Enter stirng:")
char = input("Enter character to count:")
count = Counter(test_str)
print("Each character count is : \n ",count)
print(f"Count of {char} in given string is :{count[char]}")