# Convert kmph to MPh and commited


def conv(data1):

    data_con = 0.6214*data1
    return data_con

data_cel= int(input("Enter the Km/H: "))
print ("KM/P entered : ", data_cel)

print("The data converted to m/P is ", conv(data_cel))