#
# here is an array [138, 589, 10 ,2, 39, 8]
# write a Insertion Sort
#

a = [138, 589, 10 ,2, 39, 8]
print(a)




for i in range(1, len(a)):  # would loop from 1~5. yes, len(a) is 6, but range is 1~5
  for j in range(i-1, -1, -1): # reverse range, if i is 4, then this is 3,2,1,0
    if a[i] < a[j]: # i smaller then preview one?
      a[j], a[i] = a[i], a[j] # if so, swap
      i -= 1 # if you forgot this line, insertion sort wouldn't work
      # everytime j and i both would -1

# assume i is 4
# then j is 3,2,1,0
# without i-=1   the comparsion would become 
# 4 < 3? 
# 4 < 2? 
# 4 < 1?
# that's not what we want.
# we want 4<3? 3<2?  2<1?  1<0?

print(a)

















