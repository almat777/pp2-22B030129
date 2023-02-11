a = input()
a = a.split()[::-1]
l = list()
for i in a:
    l.append(i)
print(" ".join(l))