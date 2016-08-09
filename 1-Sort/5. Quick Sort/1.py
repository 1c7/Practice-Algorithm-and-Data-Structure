def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greator = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greator)

a = [5,1,2,19,22,31,45,7]

b = quicksort(a)
print(b)
