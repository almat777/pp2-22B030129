import re

text = input()

r = re.search("ab*", text)
print(r)