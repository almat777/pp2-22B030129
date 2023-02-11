def hist(lol):
    for i in lol:
        print(i * "*")
n = int(input())
l = list()

for i in range(n):
    x = int(input())
    l.append(x)
hist(l)