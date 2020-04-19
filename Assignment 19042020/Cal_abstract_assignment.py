#abstract class calculator

from abc import ABC,abstractmethod

class Calculations(ABC):
    print ("This is calculations class")
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def mul(self):
       pass

class numbercalculator(Calculations):
    def __init__(self):
        print ("This is number class ")
        self.num1 = int(input("Enter the first number : "))
        self.num2 = int(input("Enter the second number :"))

    def add(self):
        print("The sum of two numbers is : ", self.num1 + self.num2)
    def mul(self):
        print("The multiplication of two numbers is : ", self.num1 * self.num2)

class stringcalculator(Calculations):
    def __init__(self):
        print ("This is String class ")
        self.str1 = input("Enter the first String : ")
        self.str2 = input("Enter the second String : ")

    def add(self):
        print("The sum of two strings is : ", self.str1 + self.str2)

    def mul(self):
        try:
            if (self.str1.isdigit()== True and self.str2.isdigit()== True):
                answer = int(self.str1) * int(self.str2)

            print("The multiplication of two strings is : ", answer)

        except:
            print("Cannot multiply two strings that are not integers")

numcal1=numbercalculator()
numcal1.add()
numcal1.mul()


stringcal1=stringcalculator()
stringcal1.add()
stringcal1.mul()