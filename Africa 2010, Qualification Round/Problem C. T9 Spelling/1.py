
# input
small = 'C-small-practice.in'
large = 'C-large-practice.in'
in_file = open(small, 'r')
in_file = open(large, 'r')

# output
output_filename = 'result.txt'
out_file = open(output_filename, 'w')

# start read
test_case = in_file.readline()
test_case = int(test_case)
print(test_case)



pad = {
  ' ' : [0, 1],
  # number, position
  'a' : [2, 1],
  'b' : [2, 2],
  'c' : [2, 3],

  'd' : [3, 1],
  'e' : [3, 2],
  'f' : [3, 3],

  'g' : [4, 1],
  'h' : [4, 2],
  'i' : [4, 3],

  'j' : [5, 1],
  'k' : [5, 2],
  'l' : [5, 3],

  'm' : [6, 1],
  'n' : [6, 2],
  'o' : [6, 3],

  'p' : [7, 1],
  'q' : [7, 2],
  'r' : [7, 3],
  's' : [7, 4],

  't' : [8, 1],
  'u' : [8, 2],
  'v' : [8, 3],

  'w' : [9, 1],
  'x' : [9, 2],
  'y' : [9, 3],
  'z' : [9, 4]
}

for i in range(1, test_case+1):
  line = in_file.readline().replace('\n','')

  # if line == '':
  #   s = "Case #"+str(i)+":"+' '
  #   out_file.write(s)
  #   out_file.write('\n')
  #   continue

  result = ''
  last_char_number = None
  for one in line:
    char_info = pad[one]
    keynumber = str(char_info[0])
    keyposition = int(char_info[1])

    if last_char_number != None and keynumber == last_char_number:
      result += ' ' # wait

    result += keynumber * keyposition  # in python 's'*3 = 'sss'
    last_char_number = keynumber

  # print(result)
  s = "Case #"+str(i)+":"+' '+result
  print(s)
  out_file.write(s)
  out_file.write('\n')
  # break
