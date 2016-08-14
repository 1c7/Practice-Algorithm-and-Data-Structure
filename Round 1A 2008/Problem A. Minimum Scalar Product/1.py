
# input
small = 'A-small-practice.in'
large = 'A-large-practice.in'
# in_file = open(small, 'r')
in_file = open(large, 'r')

# output
output_filename = 'result.txt'
out_file = open(output_filename, 'w')

# start read
test_case = in_file.readline()
test_case = int(test_case)


def cal(vector1, vector2):
  if len(vector1) == 1:
    return scalar_product(vector1, vector2)

  vector1 = sorted(vector1, reverse=True) # sort from big to small
  vector2 = sorted(vector2) # sort from big to small
  return scalar_product(vector1, vector2)

def scalar_product(vector1, vector2):
  final = 0
  for i in range(0, len(vector1)):
    final += vector1[i] * vector2[i]
  return final


for i in range(1, test_case+1):
  vector_number = in_file.readline()
  vector1 = in_file.readline().replace('\n','').split(' ')
  vector2 = in_file.readline().replace('\n','').split(' ')

  vector1 = list(map(lambda x: int(x), vector1))
  vector2 = list(map(lambda x: int(x), vector2))

  result = cal(vector1, vector2)
  s = "Case #"+str(i)+":"+' '+str(result)
  print(s)
  out_file.write(s)
  out_file.write('\n')