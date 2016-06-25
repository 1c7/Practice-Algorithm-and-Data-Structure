#
# here is an array [85, 2, 131, 48, 0 , 9, 7, 3, 66]
# write a Shell Sort
#
# this one is most easy to understand, (at least for me)

a = [85, 2, 131, 48, 0, 9, 7, 3, 66] # 9 element
print(a)


length = len(a)
gap = length//2  # get a init gap, we gonna change this later
                 # gap would be something like 4,2,1,0   or  7,3,1,0

while gap > 0:

  # for gap one
  if gap == 1: # just insertion sort here
    for i in range(1, len(a)): 
      for j in range(i-1, -1, -1): # compare with all element before i
        if a[i] < a[j]:            # 
          a[j], a[i] = a[i], a[j] 
        i -= 1 # if not include this line, compare would wrong 
    print('after gap',gap,a)
    break

  # for gap not one  # following comment assume this is first loop
  for i in range(length - gap):# len 9, index 0~8, gap 4, then max element is 5
      # here max index is 4, because 9 - 4 = 5, but range() is < end not <= end
      if a[i] > a[i+gap]:                # compart with gap distant
         a[i], a[i+gap] = a[i+gap], a[i] # swap
  print('after gap',gap,a)
  
  gap = gap//2   # !!! 
  #
  # note 'gap' var here eventnally become 0, in last while loop, gap == 1
  #  

print(a)



