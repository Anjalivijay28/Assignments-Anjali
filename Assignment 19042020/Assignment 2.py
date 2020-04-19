#create calculator and area
#commit


class calculator:
    # num1 = input("Enter the first number : ")
    # num2 = input("Enter the second number : ")
    print("This is Calculator class")
    def __init__(self):
        self.num1= int(input("Enter the first number : "))
        self.num2= int(input("Enter the second number : "))
        self.operator = input("Enter the operator : ")

    def calc(self):

        try:
            if (self.operator == '+'):
                answer = self.num1 + self.num2
            elif (self.operator == '-'):
                answer = self.num1 - self.num2
            elif (self.operator == '*'):
                answer = self.num1 * self.num2
            elif (self.operator == '/'):
                answer = self.num1 / self.num2

            print("The answer is : ", answer)

        except ZeroDivisionError:
            print("The second number is Zero. Please provide non zero value.")
        except:
            print("Incorrect operator")

class Area():
    print("Area class")
    def __init__(self):
        print("Area class")
    def area_rec(self):
        self.len = int(input("Enter the length of rectangle : "))
        self.breadth = int(input("Enter the breadth of rectangle : "))
        answer=self.breadth*self.len
        print("The Area of rectangle is : ", answer)

    def area_square(self):
        self.squarelen = int(input("Enter the length of square : "))
        answer=self.squarelen*self.squarelen
        print("The area of square is : ", answer)

class Multipurpose(calculator,Area):
    print("This is multipurpose class")

# c1=calculator()
# c1.calc()
#
# a1= Area()
# print ("This is calculation of area")
# a1.area_rec()
# a1.area_square()

mul1=Multipurpose()
mul1.calc()
mul1.area_square()
mul1.area_rec()