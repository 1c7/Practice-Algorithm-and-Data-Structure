# usr/bin/python3
# https://code.google.com/codejam/contest/6254486/dashboard#s=p0
'''
  Google Code Jam 2016
  Qualification Round
  Problem A
'''

import sys
try:
    file_full_path = sys.argv[1]
    print (file_full_path)
except:
    exit()

# input file
f = open(file_full_path, 'r');

# output file
output_filename = file_full_path.split('.')[0] + '.out'
print (output_filename)
out = open(output_filename, 'w');


total_test_cast = f.readline()
must_seen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in range(0,int(total_test_cast)):
	one_line = f.readline()  
	#print(one_line)
	one_line = one_line.strip()
#	if one_line == "1":
	#  print("1")
	 # sys.exit()
	num = int(one_line) 
	if num == 0:
		out.write("Case #" + str(x+1) + ":" + "INSOMNIA")
		out.write("\n")
		continue
	time = 2
	while must_seen:
    # check one_line len
		for a in str(one_line):   #must a result, either INSOMNIA or some number
			if a == '\n':
				continue
			a = int(a)
			try:
				must_seen.remove(a)
			except Exception as e:
				pass
		if must_seen:
			one_line = time * num
			time = time +1
			#print(time)
			#one_line = str(a)
	#print("empty!!")
	#print(one_line)
	out.write("Case #" + str(x+1) + ":" + str(one_line))
	out.write('\n')
	continue

f.close()
out.close()
