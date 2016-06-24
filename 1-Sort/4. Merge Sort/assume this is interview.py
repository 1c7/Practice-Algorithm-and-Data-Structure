#
# hi here is array [19, 28, 57, 3, 0, 62, 1]
# please write a Merge Sort
#
a = [19, 28, 57, 3, 0, 62, 1] # 7 element
print(a)
print()

#
# divide
#
def merge_sort(l):
  print(l)
  if len(l) < 2: # base case
    print('-', l)
    return l
  mid = len(l) // 2
  left = l[:mid]
  right = l[mid:]
  print(left, right)
  left_result = merge_sort(left) #recursive
  right_result = merge_sort(right) #recursive
  return merge_v2(left_result, right_result)

#
# merge
#
def merge(left, right):
  print('merge', left, right)
  # one of them could be empty, so we return other one that are not empty
  if not left:
    return right
  if not right:
    return left

  # if got here, that mean both left and right are not empty
  i = 0
  j = 0
  result = []
  while (len(result) < len(left) + len(right)): # result < left+right
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
    if i == len(left) or j == len(right): # if one finger is at end
      result.extend(left[i:] or right[j:])# put not empty one append to 'result'
      break 
  print('merge result', result)
  return result

#
# merge version2
# I would likt to call it 'finger' version
#
def merge_v2(left, right):
  print('merge', left, right)
  # one of them could be empty, so we return other one that are not empty
  if not left:
    return right
  if not right:
    return left

  # if got here, that mean both left and right are not empty
  i = 0
  j = 0
  # imagine i,j are finger
  result = []
  while i < len(left) and j < len(right): # if both finger is not at end
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  # i or j, one of them is at end, so loop out, execute here.
  # other one still have value, so:
  while i < len(left):
      result.append(left[i])
      i=i+1 # if you don't write this, you would stock in this loop
  while j < len(right):
      result.append(right[j])
      j=j+1
  # just check which one is not empty, that mean there are remain one value 
  # append it
  print('merge result', result)
  return result










b = merge_sort(a)
print()
print(b)








