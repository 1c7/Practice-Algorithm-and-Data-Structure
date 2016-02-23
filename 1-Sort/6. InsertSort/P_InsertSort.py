
a = [9, 7, 3, 2, 6, 88]
print(a)

def insert_sort(lists):
    count = len(lists)
    for i in range(1, count): # 循环生成索引
        key = lists[i]  # 当前这个
        j = i - 1 # 前一个的索引
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

b = insert_sort(a)
print(b)

