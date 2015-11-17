

'''


Data Structures and Algorithms in Python

p261

栈：单链表实现





'''


    
class LinkedStack:

    # --------------- 内嵌的节点 class -------------
    class _Node:
        __slots__ = '_element', '_next'
        '''
         slots 的用途是限制死 class 的属性
         http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868200605560b1bd3c660bf494282ede59fee17e781000

         Data Structures and Algorithms in Python
         这本书的 99 页有写
    
        '''
        
        def __init__(self, element, next):
            self._element = element
            self._next = next
        
    # ---------------- stack method -------------
    def __init__(self):
        # 弄个空栈 
        self._head = None # 引用头节点
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1
        # 就两行代码

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element
    
    def pop(self):
         if self.is_empty():
            raise Empty('Stack is empty')
         answer = self._head._element
         self._head = self._head._next
         self._size -= 1
         return answer



S = LinkedStack()
S.push('c')
S.push('s')

print(S.pop())








































        
