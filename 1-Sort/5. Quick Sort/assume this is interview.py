#
# hi here is array [47, 52, 336, 1, 0, 2, 8]
# please write a Quick Sort
#
a = [47, 52, 336, 1, 0, 2, 8]
print(a)
print()

# this one is much more easy to understand then most code you found on internet
def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1: 
        pivot = array[0] # just choose a pivot
        for x in array: 
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return sort(less) + equal + sort(greater)
    # Note that you want equal ^^^^^ not pivot
    else: 
        return array 
        # because this is recursive, so this len > 1 is necessary base case

print()
print(sort(a))








