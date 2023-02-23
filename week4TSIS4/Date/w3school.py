import datetime

x = datetime.datetime.now()
print(x)
print()
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
print()

x = datetime.datetime(2020, 5, 17)

print(x)
print()

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))