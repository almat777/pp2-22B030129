def even(n):
    for i in range(1,n):
        if i%2==0:
            yield i
a = int(input())
for  x in even(a):
    print(x)