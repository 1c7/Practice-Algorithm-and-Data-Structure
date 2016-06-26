#
# here is an array [2,7,26,25,19,17,1,90,3,36]
# please write a Radix Sort
# https://www.youtube.com/watch?v=YXFI4osELGU

a = [10,15,1,60,5,100,25,50]
print (a)
print()

# ===============================
#
# biggest number?
#
# ================================
biggest = a[0]
for i in range(1, len(a)):
  if a[i] > biggest:
    biggest = a[i]
#print(biggest)


# ===============================
#
# how many digit in biggest number?
#
# ================================
how_many_digit = len(str(biggest))
#print(how_many_digit)


# ===============================
#
# padding 0 to the left. make all number have same digit as biggest number
#
# ================================
for i in range(0, len(a)):
  current_digit = len(str(a[i]))
  if current_digit < how_many_digit:
    lack_digit = how_many_digit - current_digit
    a[i] = "0" * lack_digit + str(a[i])
  else:
    a[i] = str(a[i])
print(a)
print()




#
# start "sorting"
#
for i in range(-1, -1-how_many_digit, -1): 
  # i == -1,-2,-3....
  
  # create enought bucket
  print(i)
  bucket = [[] for _ in range(10)]

  # put number from list in bucket
  for j in a:
    digit = int(str(j)[i]) # here we use 'i' get last x digit
    bucket[digit].append(j)
  print(bucket)

  # one round over
  # clear 'a', loop though bucket, 
  # put number from bucket back to list
  a = []  
  for innerlist in bucket:
    for item in innerlist:
        a.append(item)
  print('pass ', i, a)
  print()


print(a)
print()


#
# remove these 0
#
for i in range(len(a)):
  a[i] = int(a[i])


print(a)
print()







