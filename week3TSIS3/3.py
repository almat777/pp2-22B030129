def solve(numheads, numlegs):
    Chicken = numheads - ((numlegs - 2*numheads)/2)
    Rabits = numheads - Chicken
    return Chicken, Rabits
a = int(input())
b = int(input())
print(solve(a,b))