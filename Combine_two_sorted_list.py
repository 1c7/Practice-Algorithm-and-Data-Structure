# coding=utf-8

'''

# combine two list that already sorted
x = [1, 9, 13, 20, 100, 999]
y = [2, 8, 8888]
i = 0;
j = 0;
z = []

print(x)
print(y)

# print(sorted(x+y))
# python 自带的函数来结合2个数组并排序
# https://docs.python.org/2/howto/sorting.html


for i in range(0, len(x)):
  if x[i] < y[j]:
    z.append(x[i])
  else:
    z.append(y[j])
    j = j+1
  
  
print(z)




sys.exit("____________quit________________")
'''
