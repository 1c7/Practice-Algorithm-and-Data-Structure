from collections import OrderedDict  # default python dict doesn't maintain any order

# input
small = 'B-small-practice.in'
large = 'B-large-practice.in'

in_file = open('example.in', 'r')
# in_file = open(small, 'r')
# in_file = open(large, 'r')



# output
output_filename = 'result.txt'
out_file = open(output_filename, 'w')

# start read
test_case = in_file.readline()
test_case = int(test_case)
# print(test_case)


def tell_me_batch_or_impossible(N_milkshake, M_customer):

  imp = 'IMPOSSIBLE'
  batch = OrderedDict() # record flavor and type
  
  for i in range(1, N_milkshake+1):
    i = str(i)
    batch[i] = None

  all_customer = []
  for customer_number in range(1, M_customer+1):   # process customer one by one
    one_customer = in_file.readline().replace('\n','').split(' ')  # one customer(one line), turn into list
    all_customer.append(one_customer)

  for one_customer in all_customer:
    how_many_type_customer_like = int(one_customer.pop(0))


    for i in range(0, len(one_customer), 2):
      flavor = one_customer[i]
      melt   = one_customer[i+1]
      
      if batch[flavor] == None and melt == '0':
        batch[flavor] = melt
      elif batch[flavor] == None and melt == '1' and i+1 != len(one_customer)-1:
        continue
      elif batch[flavor] == None and melt == '1' and i+1 == len(one_customer)-1:
        batch[flavor] = melt

      if batch[flavor] == '0' and melt == '0':
        break
      elif batch[flavor] == '0' and melt == '1' and i+1 != len(one_customer)-1:
        continue
      elif batch[flavor] == '0' and melt == '1' and i+1 == len(one_customer)-1:
        return imp
    
      if batch[flavor] == '1' and melt == '1':
        break
      elif batch[flavor] == '1' and melt == '0' and i+1 != len(one_customer)-1:
        continue
      elif batch[flavor] == '1' and melt == '0' and i+1 == len(one_customer)-1:
        return imp


  fin = ''
  for one in batch:
    if batch[one] == None:
      fin += '0'
    else:
      fin += batch[one]
    fin += ' '
  return fin
    


# def skip_n_line(n):
#   for i in range(0, n):
#     in_file.readline()


for i in range(1, test_case+1):
  N_milkshake = in_file.readline()
  M_customer = in_file.readline()

  N_milkshake = int(N_milkshake)
  M_customer = int(M_customer)
  # print('Milkshake number: ', N_milkshake)
  # print('Customer number: ' , M_customer)
  
  result = tell_me_batch_or_impossible(N_milkshake, M_customer)
  # print(result)
  s = "Case #"+str(i)+":"+' '+str(result)
  print(s)
  # print()
  out_file.write(s.strip())
  out_file.write('\n')