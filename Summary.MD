## 总结








### 怎么表示图?
图分为：有向图，无向图  

vertex 是节点  
edge 是连接的线  

the “degree” of a node is the number of neighbors  
     无向图节点的 degree 就只是邻居的数字而已  
     有向图节点的 degree 分为 in-degree 和 out degree  

__图有两种表示法__

1 Adjacency List 有两列（竖的列）用于表示无向图  
     一个 column 是节点名字  
     另一个 column 是所有邻近节点的列表（顺序不重要）  

| name | ajust node
----|------
|1| 2,3,4
|2| 1
|3| 2,4




2 Adjacency  Matrix  
     对于有4个节点的图，那么有四行四列  
     如果有100个节点，那就是100行100列  
     那么我们现在有个网格，  
     在网格里放 0 和 1 代表是有没有连接  
    
     可以用来表示 有向图 和 无向图  

如果图里的 edge 少，那么用 List 比较好，如果 edge 很多，就用 Matrix  
请思考下为什么    

总结，要么两列，要么网格    




<br/>
1. 深度优先搜索是一直往子节点下跑, 没有子节点了再上去, 再看看上面那一个有没有没访问过的子节点.  
2. 广度优先就是找邻居..  一层一层的找  

3.  树的例子:  
    文件系统  
    族谱  
    比赛晋级图  
    

4. 二叉树 = 最多2个子节点, 一个左边一个右边. 允许只有左子节点或者只有右子节点, 并不是说除了叶节点之外其他节点都要有2个子节点才算  

<br/>
5. 二叉树下面有两类: 满二叉树, 完全二叉树.

<br/>
6. 满二叉树 = 全都有2个子节点, 深度一致  

<br/>
7. 完全二叉树 = 全都有2个子节点, 深度不一致  

<br/>
8. 堆是一种特殊的完全二叉树  
当一颗完全二叉树, 上级节点都比子节点小的时候, 叫做__最小堆__  
当一颗完全二叉树, 上级节点都比子节点大的时候, 叫做__最大堆__  

<br/>
堆有什么用?  
想从一堆数字里面找出最小的, 数组要遍历, 而最小堆直接拿根节点就是了  
假设现在要插入一个数字到堆里, 就根据大小, 从根节点开始, 向下比较, 找到合适的节点就插入成子节点就行了.

插入堆可以用__向上调整__或者__向下调整__  
向上调整和向下调整的区别是啥?  




### 栈 Stack
  抽象数据结构，并不和某个特定编程语言绑定  
  数据先入后出，或者说后入先出，一回事。  
  需要提供的功能:  
  pop()  
  push()  
  实现方法：    1 数组  2 链表               

### 队列 Queue
  抽象数据结构，并不和某个特定编程语言绑定  
  数据先入先出，和现实世界中排队是一模一样的，很好理解。  
  enqueue()  
  dequeue()  
  实现方法：    1 数组  2 链表               

### 优先队列 Priority Queue
  和队列一样，不过每个值会有一个 priority  
  priotity 高的先服务  
While priority queues are often implemented with heaps, they are conceptually distinct from heaps. A priority queue is an abstract concept like "a list" or "a map"; just as a list can be implemented with a linked list or an array, a priority queue can be implemented with a heap or a variety of other methods such as an unordered array.





