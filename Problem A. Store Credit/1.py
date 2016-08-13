



small = 'A-small-practice.in'
large = 'A-large-practice.in'

in_file = open(large, 'r')

output_filename = 'result.txt'
out_file = open(output_filename, 'w')

test_case = in_file.readline()
test_case = int(test_case)


def cal(credit, num_of_item, price_list):
  credit = int(credit)
  num_of_item = int(num_of_item)
  price_list = price_list.replace('\n','').split(' ')
  print(credit)
  print(num_of_item)
  print(price_list)
  for i in range(0,num_of_item):
    for j in range(0, num_of_item):
      if i!=j and int(price_list[i]) + int(price_list[j]) == credit:
        return compare_and_return(i, j)


def compare_and_return(i, j):
  i = i+1
  j = j+1
  if i > j:
    return str(j) + ' ' + str(i)
  else:
    return str(i) + ' ' + str(j)
  

for i in range(1, test_case+1):
  credit = in_file.readline()
  num_of_item = in_file.readline()
  price_list = in_file.readline()

  result = cal(credit, num_of_item, price_list)
  s = "Case #"+str(i)+":"+' '+result
  print(s)
  out_file.write(s)
  out_file.write('\n')
