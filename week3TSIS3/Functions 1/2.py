'''Read in a Fahrenheit temperature. Calculate and display
the equivalent centigrade temperature.
The following formula is used for the conversion: C = (5 / 9) * (F – 32)'''
def sun(a):
    c = (5/9)*(a-32)
    return c
a = int(input())
print(sun(a))
