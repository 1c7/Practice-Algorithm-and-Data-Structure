









count = len(a) # 7
#print(count)
step = 2
group = count // step # 7//2 == 3
#print(group)

# no matter len(list) how big,  //= eventually gonna be 1
while group > 0:
    print(group) # 3
    for i in range(0, group): # 0
        j = i + group   # j = 0+3 = 3
        while j < count:  # 3 < 7
            k = j - group  # k = 3-3 = 0
            key = a[j]
            while k >= 0:
                if a[k] > key:
                    a[k + group] = a[k]
                    a[k] = key
                k -= group  
            j += group # j += 3
    group //= step

print()
print(a)

def shellSort(items):
    inc = len(items) // 2
    while inc:
        for i in xrange(len(items)):
            j = i
            temp = items[i]
            while j >= inc and items[j-inc] > temp:
                items[j] = items[j - inc]
                j -= inc
            items[j] = temp
        inc = inc/2 if inc/2 else (0 if inc==1 else 1)

#a = [35, -8, 11, 1, 68, 0, 3];
#shellSort(a)
#print a # [-8, 0, 1, 3, 11, 35, 68]




