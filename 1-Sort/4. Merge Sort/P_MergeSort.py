# coding=utf-8
# python 3
import sys
# for sys.exit()


#print(8//2)  # 4
#print(8/2)   # 4.0
# 2个斜杠和1个斜杠的除法有啥不同?
# // 返回整数　　／返回小数
# http://stackoverflow.com/questions/14444520/two-forward-slashes-in-python
# 在 Python3 里即使2个数字都是整数, 一个斜杠除完之后返回的也是浮点数
# 


#print(7//2) # 3
#print(5//3) # 1
#

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1: # 如果长度大于1
        mid = len(alist)//2 
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        # 切成左右两半
        
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






alist = [9, 8, 1, 22, 3]
mergeSort(alist)
print(alist)
# 可以原地操作
















