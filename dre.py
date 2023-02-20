a = int(input())
b = 0
for i in range(0,a+1):
    for j in range(1,(a-i)-1):
        print(end=" ")
    while(b != (2*i-1)):
        print("*", end="")
        b+=1
    b = 0
    print()