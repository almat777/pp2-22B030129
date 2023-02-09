def print(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        return True
n = int(input())
l = list()
for i in range(n):
