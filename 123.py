def myfunc(r):
    new = []
    for i in range(len(r)):
        x = False
        for j in range(len(r)):
            if r[i] == r[j]:
                if i != j:
                    x = True
        if x != 1:
            new.append(r[i])
    return new
n = int(input()) ; l = list()
for i in range(n):
    g = int(input())
    l.append(g)
print(myfunc(l))



