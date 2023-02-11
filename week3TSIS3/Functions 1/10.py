def gen(den):
    new =[]
    for i in range(len(den)):
        f = False
        for j in range(len(den)):
            if den[i] == den[j]:
                if i != j:
                    f = True
        if f != 1:
            new.append(den[i])
    return new
l = list()
n = int(input())
for i in range(n):
    x = int(input())
    l.append(x)
print(gen(l))