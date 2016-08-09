### 常见术语
### Vertex/Node 是图里的节点  
### Edge 是图里的线  
### Weight 是 Edge 的权重  
### Degree 是 邻居数量， the degree of a node is the number of neighbors，有向图节点的 degree 分为 in-degree 和 out degree

### 图的分类：有向图，无向图。


### 图可以解决的问题:  
  1 地图的最短路径导航  
  2 最短电线距离  
  3 各种短路径问题  


### 用图时要考虑的问题:
  有向图，无向图？  
  路线是否有权重？  
  是否有 Loop？  
  

### 图的 2 种表示法（最常用的） 这个视频一定要看
https://www.youtube.com/watch?v=WQ2Tzlxl_Xo&list=PLSVu1-lON6LxCmXNMfZBq7bdMAvUf3Sc7&index=2  
Coursera 有个 Algorithm Thinking Part1 的第一周里也讲了图的表示方法, 也很容易懂，我没链接你自己去 COursera 找  

#### 1 Adjacency List 有两列（竖的列）
     一个 column 是节点名字  
     另一个 column 是所有邻近节点的列表（顺序不重要）  
    主要用来表示无向图，如果要表示有向图就要取舍，是存指向我的节点，还是存我指向别人的节点。  
    vertext outgoing list, vertext ingoing list  
    或者干脆两个列表都存  
    你也可以从一个列表推出另一个列表。  
    

#### 2 Adjacency  Matrix
     对于有 4 个节点的图，那么有四行四列  
     如果有 100 个节点，那就是 100 行 100 列  
     那么我们现在有个网格，  
     在网格里放 0 和 1 代表是有没有连接  
    
     可以用来表示 有向图 和 无向图  
     如果表示无向图，有一半空间可以不用，节省下空间，因为是一样的  
     有人喜欢用上半部分表示，有人喜欢用下半部分表示


List 比起 Matrix 常用  



















