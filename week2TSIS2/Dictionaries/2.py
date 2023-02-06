thisdict =	{"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict["model"]
print(x)

x = thisdict.keys()
print(x)

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()
print(x)
car["color"] = "white"
print(x)

x = thisdict.values()
print(x)

car["year"] = 2020
print(x)

x = thisdict.items()
print(x)

x = car.values()
print(x)
car["color"] = "red"
print(x)

car["year"] = 2020
print(x)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
