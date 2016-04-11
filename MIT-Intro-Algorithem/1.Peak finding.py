# coding=utf-8
# python 3
'''
MIT
Intro to Algorithms - Lecture 1: Algorithmic Thinking, Peak Finding

http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-1-algorithmic-thinking-peak-finding/


标题: 
  Peak finding


描述:
  假设有个数组 [a, b, c, d, e, f, g]
  (这里的字母代表着数字, 数字的大小和正负不重要)
  要求找到其中的 peak, 
  peak 的意思是:

  假设 b 是 peak, 那么 b >= a 并且 b >= c
  如果是边缘情况, 比如 a 和 g
  那么只需要比较旁边的那一个元素就可以了


Problem:
  Find a peak if it exists
  找到第一个 peak 就足够了, 即使数组里有多个 peak 也不管
  
  

找到一个 blog 也是说这个的:
http://m.blog.csdn.net/blog/gaobohello1987/45666525

'''
import random



# small set test
a = [31, 90, 44, 1, 2, 6, 9, -8, 0]


# large set test
b = random.sample(range(-1, 50000), 50000)
# https://docs.python.org/2/library/random.html
# https://docs.python.org/3/library/random.html


'''
  最简单直接的解决思路是线性查找

'''
def find_peak1(l):
  if len(l) == 0:
    return False
  
  for index in range(0, len(l)):
  
    if index == 0:  
    # 如果是第一个元素
      if l[index] > l[index+1]:
        peak = l[index]
        return peak
    
    elif index == len(l):  
    # 如果是最后一个元素
      if l[index] > l[index-1]:
        peak = l[index]
        return peak   
    
    else:  
    # 如果是介于第一个和最后一个的中间的元素
      if l[index] > l[index+1] and l[index] > l[index-1]:
        peak = l[index]
        return peak     
      
    

#peak = find_peak1(a)
#print(peak)




'''

  进阶思路是二分查找
  
  直接看中间那个元素符不符合 peak 的要求
  不符合的话,看下是中间元素的左边那个元素大,还是右边那个元素大
  然后再查那半边

'''
def find_peak2(l):
  
  if len(l) == 0:
    return False
  
  if len(l) == 2:
    return max(l)
  
  peak = None  
     
  mid_index = len(l)//2  
  print()
  print(l)
  print( "mid index is "+str(mid_index) )
  print( "mid element is "+str(l[mid_index]) )
  # 向下取整 返回整数 返回中间那个数的索引
  
  
  # 如果大于两边的数
  if l[mid_index] > l[mid_index+1] and l[mid_index] > l[mid_index-1]:
    peak = l[mid_index]
    print( "peak is "+str(l[mid_index]) )
    return peak
    
  elif l[mid_index-1] > l[mid_index]:
  
    return find_peak2(l[:mid_index])
    
  elif l[mid_index+1] > l[mid_index]:
  
    return find_peak2(l[mid_index:])


p2 = find_peak2(b)
print(p2)




'''

现在来试试 2D 版本
行列数列要一致

开始的地方可以自己选
比如从左到右
从上到下

'''


a = [
  [1,  90, 87, 1],
  [31, 3,  67, 845],
  [9,  9,  44, 567],
  [31, 90, 43, 2],
  [12, 2,  40, 



