import math
def vol(rad):
    return 4 * math.pi * rad**3 / 3
rad = float(input())
print(vol(rad))