# even or odd from list

def even_odd():
    list1 = [1, 4, 5, 2, 7, 4, 9, 12, 43]
    for i in list1:
        if (i%2==0):
            print ("The number ",i, "is even")
        else:
            print("The number ", i, "is odd")


even_odd()