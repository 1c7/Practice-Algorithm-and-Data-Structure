

'''


Data Structures and Algorithms in Python

p264

队列：单链表实现





'''


    
class LinkedQueue:

    # --------------- 内嵌的节点 class -------------
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next
        
    # ---------------- stack method -------------
    def __init__(self):
        # Create an empty queue
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0


    def first(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def dequeue(self):
         if self.is_empty():
            raise Empty('Stack is empty')
         answer = self._head._element
         self._head = self._head._next
         self._size -= 1
         if self.is_empty():
             self._tail = None
         return answer

    def enqueue(self, e):
        """ Add an element to the back of queue"""
        newest = self._Node(e, None)
        
        if self.is_empty():  # 如果队列是空的

            self._head = newest   # 那么这个新节点就是 head 了

        else:  # 如果不是空的
            
            self._tail._next = newest  # 插入到尾巴节点的后面

    
        self._tail = newest
        self._size += 1


    




S = LinkedStack()
S.push('c')
S.push('s')

print(S.pop())








































        
