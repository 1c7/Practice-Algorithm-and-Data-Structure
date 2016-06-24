#
# hi here is array [19, 28, 57, 3, 0, 62]
# please write a Merge Sort
#
a = [19, 28, 57, 3, 0, 62, 1] # 7 element
print(a)

#
# divide
#
def mergesort(list):
  if len(list) < 2:
    return list
  mid = len(list)//2
  #print (list[:mid])
  #print (list[mid:])
  left = mergesort(list[:mid])
  right = mergesort(list[mid:])
  return merge(left, right)

#
# merge
#
def merge(left, right):
  # because left or right can be None
	if not len(left) or not len(right): 
		return left or right
  # smart way to say: 
  # no matter which one is empty, just return other one that are not empty

	result = []
	i, j = 0, 0  # finger point
	while (len(result) < len(left) + len(right)): # result < left+right
		if left[i] < right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			j+= 1
		if i == len(left) or j == len(right): # if one finger is at end
			result.extend(left[i:] or right[j:])# put not empty one append to 'result'
			break 
	return result


#print()
#print(mergesort(a))




#
# other way to write merge sort, 
# pretty smart, because pretty short, copy from internet
#
b = [3,1,4,6,2,5]
print(b)
def mergesort2(seq): 
    mid = len(seq)//2 
    print(mid)
    lft, rgt = seq[:mid], seq[mid:]    
    print(lft, rgt)
    if len(lft) > 1: lft = mergesort2(lft)  # call itself
    if len(rgt) > 1: rgt = mergesort2(rgt)  # call itself
    res = [] 
    while lft and rgt: # both not empty
        if lft[-1] >= rgt[-1]:   # left last one > right last one
            res.append(lft.pop())   # res + left?
        else: 
            res.append(rgt.pop())  # res + right?
    res.reverse()  # reverse..
    return (lft or rgt) + res # why left or right? 
    # because it maybe odd number element, then pop can't get them all,
    # there are remain one element, so we do this.

print( mergesort2(b) )





















def m_sort(lst):
  if len(lst) <= 1:
    return lst
  mid = len(lst) // 2       # divide
  left = m_sort(lst[:mid])  # recursive, return from len <=1
  right = m_sort(lst[mid:]) # recursive, return from len <=1
  return m_merge(left, right)

# assume left is [19, 28]  right is [57, 3]
def m_merge(left, right):
    print(left, right)
    # some time you got empty stuff, so you return not empty stuff back
    if not left:
        return right
        # if left is empty, we can only return right
    if not right:
        print ('-',left)
        return left
        # same here
    if left[0] < right[0]:
        return [left[0]] + m_merge(left[1:], right)
    return [right[0]] + m_merge(left, right[1:])
    # simliary to if else, but use return
        



