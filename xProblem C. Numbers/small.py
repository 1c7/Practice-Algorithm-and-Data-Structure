# from collections import OrderedDict  # default python dict doesn't maintain any order
import math
# input
small = 'C-small-practice.in'
large = 'C-large-practice.in'

# in_file = open('example.in', 'r')
in_file = open(small, 'r')
# in_file = open(large, 'r') # number too big. overflow



# output
output_filename = 'result.txt'
out_file = open(output_filename, 'w')

# start read
test_case = in_file.readline()
test_case = int(test_case)

from decimal import *
getcontext().prec = 1024


def cal(x):
  # x = int(x)
  # a = 3 + Decimal(5).sqrt()
  result =  (Decimal(3) + Decimal(5).sqrt()) ** Decimal(x)
  l = str(result).split('.')
  return l[0][-3:].zfill(3)


# print(cal(5))

for i in range(1, test_case+1):
  one_case = in_file.readline()
  # print(one_case)
  
  result = cal(one_case.replace('\n',''))
  # print(result)
  s = "Case #"+str(i)+":"+' '+str(result)
  print(s)
  out_file.write(s.strip())
  out_file.write('\n')