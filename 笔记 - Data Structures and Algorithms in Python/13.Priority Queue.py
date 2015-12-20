'''

优先队列是什么，有什么用？

第六章的队列就和生活中排队一样，先入先出。
但实际中不一定总是这样，比如机场的降落管控中心
会基于多种情况来决定谁先落地。

某些情况先入先出是合理的，但其他时候，有优先级才行。

优先队列是队列的升级版。。

Priority queue = P

P.add(k, v)    插入到队列里, k = key, value = v

P.min()        返回一个 tuple, 就是那个 key 最小的，但并不从队列中移除

P.remove_min()  和上面那个一样, 不过从队列中移除。如果队列空就报错

P.is_empty()  如果队列为空返回 True

len(P) 返回元素个数



composition design pattern



'''




class PriorityQueueBase:

    class _Item:
        __slots__ = '_key','_value'

        def __init__(self. k. v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0



class UnsortedPriorityQueue(PriorityQueueBase):

    # 找最小,
    # 其实就是遍历找最小
    def _find_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
    while walk is not None:
        if walk.element() < small.element()L
            small = walk
        walk = self._data.after(walk)
    return small

    def __init__(self):
        self._data = PositionalList()

    def __len__(self)
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self.Item(key, value))

    def min(self):
        # p367




















        

























