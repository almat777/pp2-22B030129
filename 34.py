class Human:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def printInfo(self):
        print(self.color, self.number)

class Parent1(Human):
    def __init__(self, color, number, word):
        Human.__init__(self, color, number)
        self.word = word

    def printInfo(self):
        print(self.color, self.number, self.word)


class Parent2(Human):
    def __init__(self, color, number, word):
        Human.__init__(self, color, number)
        self.word = word

    def printInfo(self):
        print(self.color, self.number, self.word)


class Baby(Human):
    def __init__(self, color, number, word):
        Human.__init__(self, color, number)
        self.word = word

    def printInfo(self):
        print(self.color, self.number, self.word)


ret = Parent1("Tazhibaeva ", "1", "beau")
ret2 = Parent2("Raushan", "8", "tiful")

ret3 = Baby(ret.color + ret2.color, ret.number + ret2.number, ret.word + ret2.word)
ret3.printInfo()