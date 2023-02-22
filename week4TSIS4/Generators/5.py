def reverse(n):
    while n >= 0:
        yield n
        n -= 1
a = int(input())
for x in reverse(a):
    print(x)
