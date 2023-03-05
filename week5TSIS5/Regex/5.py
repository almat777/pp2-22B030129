import re

text = "asb assl assdsds "
r = re.findall(r"a.*b",text)
print(r)