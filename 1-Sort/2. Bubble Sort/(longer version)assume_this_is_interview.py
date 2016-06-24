#
# Interviewer ask a simple question:
# here is an array [1, 9, 44, 37, 8]
# write a Bubble Sort now, 
#

a = [1, 9, 44, 37, 8]
print(a)



def bubble_sort_1():
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            print(i,j)
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
# not exactly bubble sort, 
# but work
# because it compare 0->1,2,3,4 and then 1->2,3,4 
# actually more like "sink sort"
# even you reverse this by range(len(a), 0), still same, just compare 4->3,2,1,0 and then 3->2,1,0



def bubble_sort_2():
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(a)):
            if i == len(a)-1:
                continue
            if a[i] > a[i+1]:
                sorted = False
                a[i], a[i+1] = a[i+1], a[i] 
# not exactly bubble sort, 
# but work
# because it loop though array entirely everytime
# you can optimize this by -1 every loop     


def bubble_sort_3():
    sorted = False
    le = len(a)-1
    print('le = ', le)
    while not sorted:
        sorted = True
        for i in range(0, le): # first time loop from 0~3, because we compare i with i+1, so we only need 3 here 
            #print("compare ", a[i], a[i+1])
            print("compare index", i, i+1)
            if a[i] > a[i+1]:
                sorted = False
                a[i], a[i+1] = a[i+1], a[i] 
                #print(a)
        le = le - 1
#
# this is actually bubble sort
#
# sort = false
# le = len(a) - 1 because later we compare would use a[i+1]
# while not sort
#    sort = true  # assume
#    for i in range(0, le):
#       if a[i] > a[i+1]:
#           switch
#    le = le -1



#
#  false, len of array -1
#
#  while false
#     assume true
#     for loop compare
#         switch
#


# -----------------------------------------------------------


bubble_sort_3()
print(a)















