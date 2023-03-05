import re

text = "Ab_cd Wey rDw"
r = re.findall(r"[A-Z][a-z]+",text)
print(r)