import re

text = "a_almat in kbtu_kz"
r = re.findall(r"\b[a-z]+_[a-z]+\b",text)
print(r)