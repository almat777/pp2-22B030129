import re

text = "asb assl as,sdsds "
r = re.sub("\s", ":", text)
s = re.sub("[.]", ":", r)
t = re.sub(",", ":", s)
print(t)