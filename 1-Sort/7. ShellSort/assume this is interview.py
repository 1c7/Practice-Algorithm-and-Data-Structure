# here is an array [85, 2, 131, 48, 0 , 9, 7, 3, 66]
# write a Shell Sort
#
# this one is most easy to understand, (at least for me)

a = [85, 2, 131, 48, 0, 9, 7, 3, 66] # 9 element
print(a)

length = len(a)
gap = length//2

while gap > 0:

  # for gap one, just run insertion sort
  if gap == 1: 
    for i in range(1, len(a)): 
      for j in range(i-1, -1, -1):
        if a[i] < a[j]:   
          a[j], a[i] = a[i], a[j] 
        i -= 1 # if not include this line, compare would wrong
    print('after gap',gap,a)
    break

  # for gap not one, compare and swap by gap
  for i in range(length - gap):
      if a[i] > a[i+gap]:           
         a[i], a[i+gap] = a[i+gap], a[i] 
  print('after gap',gap,a)
  
  gap = gap//2   # !!! 

print(a)

# Shell sort just run Insertion Sort couple time.
# each time with different 'gap' number
# in contrast, normal insertion sort gap is 1 
# (it compare with number right before it, or say left to it, so gap is 1)
# logic:
'''
  length = len(list)
  gap = length // 2

  while gap > 0:
    run inseration sort here (with gap number)
    gap = gap // 2
  
  # the gap number eventually would become 0, so loop would stop
'''

