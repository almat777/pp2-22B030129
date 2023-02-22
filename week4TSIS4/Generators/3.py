def divisible(n):
    for i in range(1,n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
a = int(input())
for x in divisible(a):
    print(x)