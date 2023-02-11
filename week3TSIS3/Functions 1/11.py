def palin(a):
    b = a[::-1]
    if b == a:
        return True
    return False
a = str(input())
print(palin(a))