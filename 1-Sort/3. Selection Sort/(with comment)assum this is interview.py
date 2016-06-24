#
#
# hi, here is an array [173, 4876, 12, 1, 98]
# write a Selection Sort in 15 minute
#

a = [173, 4876, 12, 1, 98]
print()
print(a)


for i in range(0, len(a)):
  min = i     # *assume* this one is smallest, yes we use 'index' 
  # instead of 'value',  because we may need swap two element later.

  for j in range(i+1, len(a)):
    if a[j] < a[min]:  # anyone smaller than min? please?
       min = j
  
  if min != i: # if there are no smaller element, then don't swap with youself, 
  # that just doesn't make sense
    a[min], a[i] = a[i], a[min]


print()
print(a)









