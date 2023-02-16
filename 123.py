class Parent1:
  def __init__(mysillyobject, color1, number1):
    mysillyobject.color1 = color1
    mysillyobject.number1 = number1

  def myfunc(abc):
    print("Hello my name is " + abc.color1)

p1 = Parent1("Yellow", 36)
p1.myfunc()
