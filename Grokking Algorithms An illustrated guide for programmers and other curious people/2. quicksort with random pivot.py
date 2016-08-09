from random import randint

a = [99, 1, 28, 2, 500, 71, 39]

def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivot_index = randint(0,len(array)-1)
    pivot = array[pivot_index]
    array.remove(pivot)

    less = [i for i in array if i <= pivot]
    greater = [i for i in array if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort(a))

