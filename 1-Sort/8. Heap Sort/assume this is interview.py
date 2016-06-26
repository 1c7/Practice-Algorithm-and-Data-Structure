#
# here is an array [2,7,26,25,19,17,1,90,3,36]
# please turn it into "Max Heap"  MAX!
# and write a heap sort base on max heap (number from big to smaller-)
#
# if you heap index start from 0
  # by parent index, get left child node  = 2 * parent index + 1
  # by parent index, get right child node = 2 * parent index + 2
  # by child index, get parent node index = child index - 1 // 2

# if your heap index start from 1
  # parent of node at K is K / 2
  # child of node at K are 2k and 2k+1

#
# if you understand what is heap, and how heap insert, heap delete work
# then this code would be easy to understand
# otherwise, not so much.
#
a = [2,7,26,25,19,17,1,90,3,36]
print(a)
print()


def heap_insert(heap, i):
  print('append', i)

  if len(heap) == 0: # heap empty? just append and return
    heap.append(i)
    print(heap)
    return

  heap.append(i) # append first, now it is at end of heap array
  
  new_e_index = len(heap)-1 # get new element index
  parent_index = (new_e_index - 1) // 2  # get parent node index
 
  while heap[new_e_index] > heap[parent_index]: # new node bigger then parent?
    # change this compare > 
    # you can get max heap or min heap

    heap[new_e_index], heap[parent_index] = heap[parent_index], heap[new_e_index]
    # swap with parent
    
    # get new position index
    new_e_index = parent_index  # now our element in parent position
    if new_e_index == 0:
      break

    # get new parent index
    parent_index = (new_e_index - 1) // 2

    # swap with parent until it become root
    # or until it smaller then parent node

  print(heap)


#
# start building heap
#
def heapify(a):
  heap = [] # empty heap at begining
  print(heap)
  for i in a:
    heap_insert(heap, i)
  print()
  print('max heap:', heap)
  return heap


heap = heapify(a)



# =================================================
#
# now we have a heap, then we can use heap sort.
# 
# =================================================


def max_heap_remove():

  if len(heap) == 0:
    return False

  if len(heap) == 1:
    return heap[0]

  if len(heap) == 2: # if there are only two elmenet, return & remove bigger one
    if (heap[0] > heap[1]):
      max = heap[0]
      heap.pop(0)
      return max
    else:
      max = heap[1]
      heap.pop()
      return max

  max_value = heap[0]
  last_index = len(heap) - 1

  # swap root with last element
  heap[0], heap[last_index] = heap[last_index], heap[0]
  heap.pop() # remove last element

  if len(heap) == 2:  # if there are 3 element, then after pop, remain 2.
    # don't waste time on sorting these two.
    # just return
    return max_value;
  
  current_index = 0 # it swap with root, so current index is 0
  left_child_index = 1    
  right_child_index = 2

  # which child bigger?
  if heap[left_child_index] > heap[right_child_index]:
    child_bigger_one_index = left_child_index
  else:
    child_bigger_one_index = right_child_index
  
  #
  # swap until this node in right position
  #
  while heap[current_index] < heap[child_bigger_one_index]: 
    # smaller then one of bigger child node
    heap[current_index], heap[child_bigger_one_index] = heap[child_bigger_one_index], heap[current_index] 
    # Swap
    
    # after swap, we should get current node index and new parent index
    current_index = child_bigger_one_index
    left_child_index = current_index * 2 + 1
    right_child_index = current_index * 2 + 2
    
    # if left child not exists,
    if left_child_index >= len(heap)-1:
      break;

    # if left child exists, but right one not exists
    if left_child_index >= len(heap)-1:
      heap[-1], heap[-2] = heap[-2], heap[-1]
      break;
    
    # both child exists
    # 2 child, get bigger child, compare with it, and swap if nessaeary
    # which child bigger?
    if heap[left_child_index] > heap[right_child_index]:
      child_bigger_one_index = left_child_index
    else:
      child_bigger_one_index = right_child_index
  
  return max_value


#
# 
#
heap_sort_array = [] # empty for now

for x in range(len(heap)):
  heap_sort_array.append( max_heap_remove() )

print('heap sorted: ', heap_sort_array)















