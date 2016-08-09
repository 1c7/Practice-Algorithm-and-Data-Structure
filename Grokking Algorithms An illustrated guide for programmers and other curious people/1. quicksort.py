a = [99, 1, 28, 2, 500, 71, 39]

def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]

    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort(a))

