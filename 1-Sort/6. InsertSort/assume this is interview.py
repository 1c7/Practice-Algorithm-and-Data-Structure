#
# here is an array [138, 589, 10 ,2, 39, 8]
# write a Insertion Sort
#

a = [138, 589, 10 ,2, 39, 8]
print(a)


for i in range(1, len(a)): 
  for j in range(i-1, -1, -1): 
    if a[i] < a[j]: 
      a[j], a[i] = a[i], a[j] 
      i -= 1 

# 
# i = 3
# j = 2,1,0

# i = 4
# j = 3,2,1,0

# i = 5
# j = 4,3,2,1,0

# you get this idea.
#

print()
print(a)









