class Parent1:
    word1 = ''
    def __init__(self,color1,number1):
        self.color1=color1
        self.number1=number1
    def print(self):
        print(self.color1,self.number1,self.word1)
    def setword1(self,word1):
        self.word1 = word1
    def getword(self):
        print(self.word1)
    def printInfo1(self):
        print(self.number1,self.color1)

class Parent2:
    word2 = ''
    def __init__(self,color2,number2):
        self.color2=color2
        self.number2=number2
    def print(self):
        print(self.color2,self.number2,self.word2)
    def setword2(self,word2):
        self.word2 = word2
    def getword2(self):
        print(self.word2)
    def printInfo2(self):
        print(self.color2,self.number2)
class baby(Parent1, Parent2):
    word3 = ''
    def __init__(self,color1,color2,number1,number2):
        Parent2.__init__(self,color2,number2)
        Parent1.__init__(self,color1,number1)
        self.number3 = number1+number2
        self.color3 = color1 + color2
    def print(self):
        print(self.color3,self.number3)
    def setword3(self):
        self.word3 = self.word1 + self.word2
    def getword3(self):
        print(self.word3)
    def printInfo3(self):
        print(self.color3,self.number3)
ret3 = baby("black","white",6,8)
ret3.printInfo3()
ret3.setword1("ryt")
ret3.setword2("jui")
ret3.setword3()
ret3.getword3()



