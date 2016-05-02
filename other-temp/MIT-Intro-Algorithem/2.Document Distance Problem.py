# coding=utf-8
# python 3

'''
 document = sequence of word
 


inner product = dot product 
内积             点积

1. split docuemtn into word
2. compute document frequence
3. dot product

'''

doc = 'the dog love dog morning with water dog dog dog'
word_list = doc.split(" ")
#print(word_list)


count_frequence = {}
for word in word_list:
  if word in count_frequence:
    count_frequence[word] = count_frequence[word] + 1
  else:
    count_frequence[word] = 1
    
print(count_frequence)










































