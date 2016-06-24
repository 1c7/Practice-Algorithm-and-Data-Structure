#
#
# hi, here is an array [173, 4876, 12, 1, 98]
# write a Selection Sort in 15 minute
#

a = [173, 4876, 12, 1, 98]
print()
print(a)



for i in range(0, len(a)):
  min = i

  for j in range(i+1, len(a)):
    if a[j] < a[min]: 
       min = j
  
  if min != i:
    a[min], a[i] = a[i], a[min]



print()
print(a)













