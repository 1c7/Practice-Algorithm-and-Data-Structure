

'''

Tree

树以层级结构存储元素


Tree = T
position = p




T.root() return the position of the root of the tree
返回根的位置??

T.is_root(p) 返回 true 如果是根节点

T.parent(p)
返回 p 的上级位置

T.num_children(p)
返回下一级的数量

T.children(p)
没懂

T.is_leaf(p)
return True 如果是叶子节点

len(T)

T.is_empty()

T.positions()
all positions

iter(T)
all elements



'''


class Tree:

    # -
    class Position:
        # 表示单个元素的位置
        
        def element(self):
            raise NotImplementedError('must be implement by sub class')
        
        def __eq__(self, other):
            raise NotImplementedError('must be implement by sub class')

        def __ne__(self, other):
            ''' return True if other does not represent the same location'''
            return not (self == other)
            # opposite of __eq__

    def root(self):
        raise NotImplementedError('must be implement by sub class')
    
    def parent(self, p):
        raise NotImplementedError('must be implement by sub class')
        

    def num_children(self, p):
        raise NotImplementedError('must be implement by sub class')


    def children(self, p):
        raise NotImplementedError('must be implement by sub class')


    def __len__(self, p):
        raise NotImplementedError('must be implement by sub class')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self, p):
        return len(self) == 0

    # 节点的深度
    # 递归得出结果
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p)) 
        


# -----------------------

'''
Let p be the position of a node of a tree T .
The depth of p is the number of ancestors of p, excluding p itself.


深度就是距离根节点有多远


binary tree
就是二叉树

每个节点最多2个下级节点
下级节点分为左和右
左下级在右下级之前


proper binary tree  - full binary tree 完全二叉树
所有节点的下级，要么0要么2

一个数学运算式子可以拆成一个完全二叉树




------


二叉树 多了三种方法

T.left(p)


T.right(p)



T.sibling(p)




'''

class BinaryTree(Tree):
    

    
def left(self, p):
        
raise NotImplementedError('must be implement by sub class')

    
def right(self, p):
        
raise NotImplementedError('must be implement by sub class')
    

    def sibling(self, p):
        
parent = self.parent(p)
        if parent is None:  # 那么意味着这个节点肯定是根节点
            return None
        
else:
            
if p == self.left(parent):
                # 如果这个节点是上级节点的左节点, 那么返回右节点
                return self.right(parent)  # 可能返回空
            
else:
                return self.left(parent)   # 可能返回空
            
    # 如果是右就返回左

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
            


'''
二叉树的属性
properties of binary tree


根节点在 level 0 , 1个节点
 level 1 有 2个节点
 以此类推

 第 n 层(level n)
 
有 2 的 n 次方个节点


'''



'''
[如何实现一棵树]
Implementing Trees




1. 用链表来做



一个节点有4个数据

   上级
   左子
   右子
   本节点存的值


更新一棵二叉树的操作:
    T.add_root(e)
    	给一棵空树创建根节点, e 是根节点存的值
    	并且返回根节点的 position
    
	如果树非空返回 error

    
T.add_left(p, e):
    
	给某个节点增加一个左子节点, 返回左子节点. 如果已经有左子节点了就返回 error
    

    
T.add_right(p, e)
    
	类似
    

    T.replace(p, e): 替换元素, 并返回之前那个元素

    T.delete(p):
    	删掉那个节点, 并替换成子节点, 并返回那个节点的值
    	如果有2个子节点就报错

    T.attach(p, T1, T2):
    
	把 T1 弄成 p 的左子树
    	   T2 弄成 p 的右子树



'''

# p320
class LinkedBinaryTree(BinaryTree):
    

    class _Node:
        # 轻量级的非公开类, 用于存储一个节点
        __slot__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent = None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        # 用于表示单个元素的位置
        def __init__(self, container, node):
            self._container = container
            self._node = node
            

        def element(self):
            return self._node._element

        
        def __eq__(self, other):
            '''Return True if other is a Position representing the same location.'''
            return type(other) is type(self) and other._node is self._node

        
        # 不知道是干嘛
        def _validate(self, p):
            if not isinstance(p, self.Position):
                raise TypeError('p must be proper Position type')
            if p._container is not self:
                raise ValueError('p dose not belong to this container')
            if p._node._parent is p._node: 
                raise ValueError("p is no longer valid")
            return p._node

        # 也不知道是干嘛
        def _make_position(self,node): 
            return self.Position(self, node) if node is not None else None
        

        
    def __init__(self):
        # 初始化一个空的二叉树
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    
    def left(self, p):
        '''Return the Position of p s left child (or None if no left child).'''  
        node = self._validate(p)  
        return self._make_position(node._left)
        
        
    def right(self, p):   
        node = self._validate(p)  
        return self._make_position(node._right)
        
    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        pass
        #p322, p344

    def _add_left(self, p, e):
        pass    

    def _add_right(self, p, e):
        pass

    def _replace(self, p, e):
        pass

    def _delete(self, p):
        pass

    def _attach(self, p, t1, t2):
        pass


#------------------------------------


#
# 基于数组来表示二叉树
# 
# p325
# 没代码的.. 只是文字


#
# 遍历树的算法
#
# p328
''''
Preorder and Postorder traversal 
先序和后序遍历

还有一种叫 beadth-first 遍历
就是一层一层的遍历

还有一种叫 inorder travresal
中序遍历

画一棵树，然后四种遍历方式，这样才更清晰些
现在还有些模糊



'''












    
