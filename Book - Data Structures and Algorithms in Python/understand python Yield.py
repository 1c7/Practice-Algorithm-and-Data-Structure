'''
yield 告诉了 python 我们定义了一个 generator



'''

# ----------------------
#
#   测试 range
#
# ----------------------

'''
r = range(0, 10)
print(r)


for i in r:
    print (i)
'''
# 结果是不包括10


#
#
# 把因数都求出来了
#
# 
def factors(n):
  results = []
  for k in range(1, n+1):
    if n % k == 0:
     print(n, k)
     results.append(k)
  return results

#a = factors(10)
#print(a)



#
#
# ,,,,
#
#
def factors(n):
  for k in range(1, n+1):
    if n % k == 0:
      yield k



a = factors(10)
print(a)



#
#
#
#
#
'''
要掌握 yield 你要知道，当你调用带有 yield 的函数时，
里面的代码并没有被执行。
只是返回了一个生成器对象


'''

















































