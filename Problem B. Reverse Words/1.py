

small = 'B-small-practice.in'
large = 'B-large-practice.in'

in_file = open(large, 'r')

output_filename = 'result.txt'
out_file = open(output_filename, 'w')

test_case = in_file.readline()
test_case = int(test_case)


for i in range(1, test_case+1):
  line = in_file.readline()
  result = line.replace('\n','').split(' ')
  result.reverse()
  result = ' '.join(result)
  s = "Case #"+str(i)+":"+' '+result
  print(s)
  out_file.write(s)
  out_file.write('\n')
