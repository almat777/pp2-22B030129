class Parent1:
    def _init_(self, color, number):
        self.color = color
        self.number = number

    def info(self):
        print("color:", self.color)
        print("number:", self.number)

    def word(self, word1):
        self.word1 = word1

    def getword(self):
        return self.word1
class Parent2:
    def _init_(self, color2, number2):
        self.color2 = color2
        self.number2 = number2

    def info(self):
        print("color2:", self.color2)
        print("number2:", self.number2)

    def word(self, word2):
        self.word2 = word2

    def getword(self):
        return self.word2
class baby_boy(Parent1,Parent2):
    def __init__(self,color3,number3,word3):
        self.color3 =
