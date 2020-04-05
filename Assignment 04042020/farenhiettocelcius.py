#calculate farenhiet to celcius and commit

def conv(data1):

    data_con = (data1-32)* (5.0/9.0)
    return data_con

data_cel= int(input("Enter the Farenhiet: "))
print ("Farenhiet entered : ", data_cel)

print("The Farenhiet conveted to celcius is ", conv(data_cel))