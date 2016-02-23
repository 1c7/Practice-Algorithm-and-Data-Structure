'''

Data Structures and Algorithms in Python

p240 或者 p262
我用的福晰阅读器，下面这个页数我实在没看懂



------------------- 队列 Queue ----------------

队列就是先入先出


最基本的操作：
    Q.enqueue(e) - 入队
    Q.dequeue()  - 出队
    Q.first()    - 访问第一个元素但不让他出队
    Q.is_empty() - 队列是否为空
    len(Q)       - 队列长度
 






----------- 把 Python 的 List 包装一下变成 Queue --------------

如何实现出队？

    pop(0) 这种出队方式非常低效
    因为它会把后面所有元素往前移
    
    解决方法可以是把出队元素弄成 None
    然后用另一个变量 f 存下标，代表队头

    这样的问题是浪费太多空间了

    最终的解决方法是循环队列
    Using an Array Circularly

    


'''



class ArrayQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY

        self._size = 0
        # 队列长度
        
        self._front = 0
        # 队头在哪里

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1



    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self.data[k] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0
        
        



q = ArrayQueue()
q.enqueue('a')
q.enqueue('7')
q.enqueue('3')
q.enqueue('a')
q.enqueue('7')
q.dequeue()



print(len(q))


'''
逻辑
    初始化时：
    一个列表 - 用来存元素
    size - 存队列里有多少个元素
    front = 队头的索引



'''

















