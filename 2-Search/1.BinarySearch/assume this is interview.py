#
# here is an array [1, 4, 12, 45, 66, 99, 120, 444]
# write a binary search find number 1
#
a = [1, 4, 12, 45, 66, 99, 120, 444]
print(a)


def binarySearch(list, target):
  print('finding: ', target)
  print()
  
  first = 0
  last = len(list)-1
  found = False
  index = False

  # first and last can overlap, but first cannot bigger then last
  while first <= last and not found:
    mid = (first+last)//2
    print('mid is', list[mid])
    if list[mid] == target:
      found = True
      index = mid
    else:
      if target < list[mid]:
        last = mid - 1
      else:
        first = mid + 1 
  # so this 'while' stop when found target, 
  # or first and last cross each other one position

  return index

target_index = binarySearch(a, 444)
print('index is: ', target_index)







