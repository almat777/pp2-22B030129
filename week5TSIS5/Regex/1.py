import re

text = input()

r = re.findall(".*ab.*", text)
print(r)