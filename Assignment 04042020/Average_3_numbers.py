# calculate the average of 3 numbers and commited


def calc(data1,data2,data3):

    print ("The numbers entered are : " , data1,",",data2,",",data3)
    calc = (data1+data2+data3)/3
    return calc


data1 = int (input("Enter the first number : "))
data2 = int (input("Enter the second number : "))
data3 = int (input("Enter the third number : "))

print ("The average is : ", calc(data1,data2,data3))