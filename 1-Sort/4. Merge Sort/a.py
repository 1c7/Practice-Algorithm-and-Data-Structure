# coding=utf-8

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1: 
        mid = len(alist)//2 
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        mergeSort(lefthalf)
        mergeSort(righthalf)
        # 递归
  
        i=0
        j=0
        k=0
        # 小于左半边的长度 and 小于右半边的长度
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        
        # 
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        
        # 
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

a = [9, 8, 1, 22, 3]
mergeSort(a)
print(a)

