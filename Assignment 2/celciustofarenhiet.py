#calculate celcius to farenhiet

def conv(data1):
    data_con = (9.0/5.0)*data1 + 32
    return data_con

data_cel= int(input("Enter the celcius: "))
print ("Celcius entered : ", data_cel)

print("The celcius conveted to farenhiet is ", conv(data_cel))