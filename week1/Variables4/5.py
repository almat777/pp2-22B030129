x = "Cola"
def myfunc():
    global x
    x = "Fanta"
    print("I love "+x)
myfunc()
print("I hate "+x)