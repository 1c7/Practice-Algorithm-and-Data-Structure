# coding=utf-8
# encoding declare : https://www.python.org/dev/peps/pep-0263/


#=============================================
#
#  这里放的代码片段有:
#
#  1. 计算代码运行时间
#  2. 随机生成数列
#  3. 
#
#
#============================================




# there are a "timeit" module for test small code snipet
# https://docs.python.org/2/library/timeit.html

import random
import time





# ______________________________
#
#   1. 计算代码运行时间
#
# ______________________________

# ========================
#
#    time.clock() 的文档
#
# ========================
#  https://docs.python.org/2/library/time.html
#  中文 http://www.runoob.com/python/att-time-clock.html
#  http://pythoncentral.io/measure-time-in-python-time-time-vs-time-clock/

# print(time.clock())


start = time.clock()

for x in range(1, 1000):
  pass
  
end = time.clock()

print(start)
print(end)
print(end - start)



# ______________________________
#
#   2. 随机生成数列
#
# ______________________________

# ====================================
#
# 生成一个随机数字列表
# 要求1. 列表长度可定 比如长度是3, 有3个元素
# 要求2. 数字范围可定 比如1~1000
# 要求3. 数字不可重复
#    [1, 9, 20, 88] 这种可以
#    [1, 1, 9, 20, 88] 这种不行
#    
# =====================================

length = 20       # 数组长度 10
num_range = 1000   # 数字范围是 0~1000


# 我这里懒得自己实现, 直接用 Python 的 random.sample
# random.sample 文档: 
# https://docs.python.org/2/library/random.html
# https://docs.python.org/3/library/random.html



unsorted = random.sample(range(1, num_range), length)
print(unsorted)















