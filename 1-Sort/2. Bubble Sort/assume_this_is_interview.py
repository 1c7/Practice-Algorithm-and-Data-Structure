#
# hi, here is an array [1, 9, 44, 37, 8]
# write a Bubble Sort now, 
# we start from simple to hard.
#

a = [1, 9, 44, 37, 8]
print(a)


sorted = False
le = len(a)-1

while not sorted:
    sorted = True
    for i in range(0, le):
        print("compare index", i, i+1)
        if a[i] > a[i+1]:
            sorted = False
            a[i], a[i+1] = a[i+1], a[i] 
    print()
    le = le - 1


print(a)















