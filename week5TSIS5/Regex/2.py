import re

text = input()
r = re.findall("ab{2,3}",text)
print(r)