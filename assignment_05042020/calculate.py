#create function to calculate

def calc(data1, data2, operator):

   try:
    if (operator == '+') :
        answer = data1+data2
    elif (operator == '-'):
        answer = data1 - data2
    elif (operator == '*'):
        answer = data1 * data2
    elif (operator == '/'):
        answer = data1 / data2

    print("The answer is : ", answer)

   except ZeroDivisionError:
       print("The second number is Zero. Please provide non zero value.")
   except:
        print ("Incorrect operator")

data1 = int(input("Enter the first digit : \n"))
data2 = int(input("Enter the first digit : \n"))
operator = str(input("Enter the operator : \n"))
calc(data1, data2, operator)