'''
  插入排序:
'''
a = [9, 7, 3, 2, 6, 88]
p a


def insert_sort(lists)

    count = lists.size
    
    for i in 0..count-1
      key = lists[i]   # 拿到当前元素
        j = i - 1      # 上一个元素的索引
        while j >= 0 do   # 跳过 0, -1  要  1, 0
            if lists[j] > key  # 如果大于上一个元素 [9,1,2,...]  
                lists[j + 1] = lists[j]   # 
                lists[j] = key
            end
            j -= 1
        end
    end
    
    return lists
    
end


b = insert_sort(a)
p a


