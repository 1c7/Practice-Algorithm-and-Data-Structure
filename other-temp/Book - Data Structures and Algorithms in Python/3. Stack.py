'''

Data Structures and Algorithms in Python

p230




----------------------- 栈 --------------------

用 Python 实现栈
栈 = 后入先出


至少有以下几个方法
    push
    pop


    top
    is_empty
    len


--------------  栈有什么用？？  -------------



书里讲了3个例子

    1.翻转字符串    扩展：翻转文件内容
    
    2.验证{}() 括号的正确嵌套   扩展：验证 HTML 的正确嵌套





-------------- 适配器模式 --------------


adapter design pattern  -  适配器模式
意思就是把现有的东西打个包，让他更好用


很多设计模式教科书都喜欢用读卡器进行举例：
手机用户常用的tf卡是不能插到电脑上工作的，
而是需要插在读卡器上，然后接驳到电脑的USB端口上，这样就能进行数据处理工作了；
同样的例子还有电源的转换器，美国的电压一般是110V，而中国大陆是220V，
如果将美国标准的电器直接插到大陆的插座上使用，势必要出现电压过高被烧毁的结果，
这时候就需要一个电压的转换器，将220V的电压转换为110V进行使用。
这些，都是适配模式以及适配器的例子。


Stack.push(e)  ==  List.append(e)

Stack.pop() == L.pop()

Stack.top == L[-1]

S.is_empty()  ==  len(L) == 0

len(s) == len(l)



-----------  我们把 Python 里的 List 打个包变成栈 ------------


'''


class Empty(Exception):
    pass




class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
            
    def __str__(self):
        return str(self._data)

'''
AS = ArrayStack()
AS.push(3)
AS.push(3)
AS.push(3)
print(AS)
'''



#==============================
# 翻转文件内容
#==============================

def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip("\n"))
    original.close()

    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()


# reverse_file('x.txt')




#=====================================
# p236
#=======================================

'''

处理配对问题
    括号正确嵌套

isMatch("()()") == correct
isMatch("()[()]") == correct
isMatch("[()()]") == correct
isMatch("(){}()") == correct
isMatch("<><") == Incorrect
isMatch("()>") == Incorrect



'''

def is_match(expr):
    lefty = '({['
    righty = ')}]'

    S = ArrayStack()
    
    for c in expr:
        # 循环每个字符
        
        if c in lefty:
            S.push(c)
            
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False

    return S.is_empty()


'''
整体逻辑：

    定义 opening symbol 和 closeing symbol
    
    循环每个字符:
    
        如果属于 opening
        
           入栈
           
        如果属于 closing
        
           栈为空吗？如果是，代表匹配不上, return false
           
           如果不为空，
             栈最后一个元素出栈，看下是否是正确的闭合标签



：看到开始标签就入栈
：直到看到结束标签才去出栈匹配

    
'''

'''
a = '{[]()}'
b = '['
if is_match(a):
    print ('match!')
else:
    print ("not!")

'''




# index 方法返回的是数字, 就是索引位置
'''
z = "plokijuh"
print(z.index('l'))
'''





'''
========================================

    判断 HTML 是否正确嵌套
    p238/p260

返回 true | false

这个只是初级版本的
如果传入空，它还是返回 TRUE
如果传入的字符串里没有 < 这个符号  也依然是 TRUE

'''


def is_matched_html(raw):
    S = ArrayStack()
    j = raw.find('<')

    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]  
        print (tag)
        # tag 存着标签里的内容 <内容>

        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()


a = "<html></html>"      # true
b = '<ssss><dddd>'       # false
c = ''                   # true
d = 'aoeufhoeuhfoauehf'  # true
e = '>afaefaefaef'       # true
f = '<body></haha>'      # false
result = is_matched_html(f)
print(result)

'''
逻辑
    先找 < 
    如果找得到就开始找 >
    如果找得到 >
    就把 <> 之间的内容获取到
    判断内容是否以 / 开头, 如果不是, 就入栈

    如果是，就看下栈里是否有匹配的
    if tag[1:] != S.pop():

    然后继续找下一个 < 
    
'''



# find 方法返回找到的第一个匹配元素的下标
# 第二个参数是开始搜索的位置, 会从那个下标开始往右搜索
#
'''
a = 'a<aaasssssss1'
b = 'asdfeafafe'

print(a.find('<', 3))
'''

















