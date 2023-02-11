def gen(den):
    for i in range(len(den)-1):
        if den[i] == den[i+1] == 3:
            return True
    return False


l = list()
n = int(input())
for i in range(n):
    x = int(input())
    l.append(x)
print(gen(l))