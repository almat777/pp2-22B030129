word = input()
word1 = reversed(word)
if list(word) == list(word1):
    print(f"Yeah {word} is a palindrome")
else:
    print(f"No {word} isn't a palindrome")
