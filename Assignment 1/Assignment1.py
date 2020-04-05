<<<<<<< HEAD
=======

#Assignment by: Anjali
#Date : 21 Mar 2020

>>>>>>> Added Assignment
# Assignment 1
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,15,18,20,24,25,27,30,32,33]
# count items divisible by 2,3,4,5,7:
# list the items as well
# items divisible by 2: []
# items divisible by 3: []
# items divisible by 4: []

list2=[]
list3=[]
list4=[]
list5=[]
list6=[]

count =0
count1=0
count2=0
count3=0
count4=0

for i in list1:
    if (i%2==0):
        list2.append(i)
        count= count+1

    if (i%3==0):
        list3.append(i)
        count1 = count1 + 1

    if (i%4==0):
         list4.append(i)
         count2 = count2 + 1

    if (i % 5 == 0):
        list5.append(i)
        count3 = count3 + 1

    if (i % 7 == 0):
        list6.append(i)
        count4 = count4 + 1

print ("Divisible by 2 :" ,count)
print ("Divisible by 3 :" ,count1)
print ("Divisible by 4 :" ,count2)
print ("Divisible by 5 :" ,count3)
print ("Divisible by 7 :" ,count4)

print ("List divisible by 2 : ", list2)
print ("List divisible by 3 : ", list3)
print ("List divisible by 4 : ", list4)
print ("List divisible by 5 : ", list5)
print ("List divisible by 7 : ", list6)