## 练算法和数据结构
文件夹和文件的命名方式都是为了方便自动补全  

数据结构是存放数据的方式,   
针对不同的问题, 用合适的数据结构搭配算法可以更快的得到答案. 


### 说明
1. 代码里会放详细的注释解释整个思路
2. 与代码同文件夹的 README.MD 会放一些好的视频,资料来源,重点讲解等等.


<br>
### 排序
##### 序号随便的, 不是按什么规则排的
|序号|名字|进度
----|------|----
|1|[桶排序 - Bucket Sort(差)](./Sort/1. Bucket Sort)| √ 
|2|[冒泡 - Bubble Sort(差)](./Sort/2. Bubble Sort)|√   
|3|[选择 - Selection Sort](./Sort/3. Selection Sort)|√  
|4|[归并 - Merge Sort](./Sort/4. Merge Sort) | 
|5|[快速 - Quick Sort](./Sort/5.InsertSort)|  
|6|[插入 - Insertion Sort](./Sort/6.InsertSort)|  
|7|[希尔 - Shell Sort]|  
|8|[堆 - Heap Sort]|  
|9|Cocktail Sort(差) also known as bidirectional bubble sort |不实现了, 没意思  
|10|梳 - Comb Sort - Comb sort improves on bubble sort.|  
|11|Timsort is a hybrid stable sorting algorithm, derived from merge sort and insertion sort|  

排序的重点: 尽可能减少比较和交换的次数  

3.4 Distribution sort
3.4.1 Counting sort
3.4.3 Radix sort



Visualization and Comparison of Sorting Algorithms  
https://www.youtube.com/watch?v=ZZuD6iUe3Pc  


最好: Shell > Quick  > Merge > Heap    
最差: Selection, Bubble Sort, Cocktail Sort  


#### 最好的排序算法  

http://cs.stackexchange.com/questions/3/why-is-quicksort-better-than-other-sorting-algorithms-in-practice
http://www.cprogramming.com/tutorial/computersciencetheory/sortcomp.html
http://betterexplained.com/articles/sorting-algorithms/
https://www.quora.com/What-is-the-fastest-sorting-algorithm

<br>
### 搜索

|序号|名字|进度
----|------|----
|1|二分查找| 
|2|深度优先算法 - Deep First Search - DFS| 
|3|广度优先算法 - Breadth First Search - BFS| 




<br>
### 树
为什么需要树? 树有什么用? 实际应用在了哪些地方?   
1. 

|序号|名字|进度
----|------|----
|1|二叉搜索树 - Binary search tree| 
|2|红黑树 - Red–black tree| 
|3|[B+树 - B+ tree](./Tree/B+ Tree)| 


<br>
### 图
1. 图有什么用? 实际应用在了哪些地方?   



Hash Table are called dict in python



<br>
### 思路


<br>
### 练习题









http://codility.com/  
http://www.codewars.com/  

Google Code Jam  
https://code.google.com/codejam  

Leet Code  
https://leetcode.com/  

Git book -- LeetCode题解  
https://www.gitbook.com/book/siddontang/leetcode-solution/details  



<br/>
算法可视化动画:  
* http://www.sorting-algorithms.com/  
* http://www.cs.usfca.edu/~galles/visualization/Algorithms.html  
* http://visualgo.net/  这个很好  
* http://zh.visualgo.net/  中文版的  

<br/>
知乎: 有哪些学习算法的网站推荐？  
http://www.zhihu.com/question/20368410

Data Structure and Algorithm notes  
https://www.gitbook.com/book/yuanbin/algorithm/details


Coursera Algorithem - Standford  
https://www.coursera.org/course/algo


JS: Interview Algorithm  
http://www.thatjsdude.com/interview/js1.html

What book about algorithms is a must read for a programmer?  
https://www.quora.com/What-book-about-algorithms-is-a-must-read-for-a-programmer


What are the 10 algorithms one must know in order to solve most algorithm problems?  
https://www.quora.com/What-are-the-10-algorithms-one-must-know-in-order-to-solve-most-algorithm-problems


<br/>

不要试图记住所有的东西.而是从基础开始,做两件事:  
__第一件事__. 把数据结构图形化,视觉化.(突然想起来我高中竞赛老师说的一句话:数形结合千般好,一旦不做万事休啊! 就是要画图! )在直觉上感受一个数据结构是什么样子的.  
使用它是什么感觉,抽象上和具体实现上是什么样子的.这就是最重要的事情.  
并且无论是对于简单的队列,栈还是天杀的平衡树都很重要而且有效.把数据结构画出来,在你的脑袋瓜里面就能想象出来,总之,你需要做的就是,直观的去了解这些数据结构.  
__第二件事__.学习什么时候用什么样的数据结构和算法.对于学生来说这很难,而且你要做作业的时候老师也没告诉你们这该怎么办.╮(￣▽￣")╭ 不过没关系. 你要认识到当你真正处理到现实问题的时候或许你才能掌握某些数据结构,比如哈希表.但是即使是个学生,你也应该知道数据结构的实用性:什么时候你需要个哈希表,什么时候你需要个树,什么时候你需要个堆? 而不是一开始就陷入到追求细节中去.  
http://www.zhihu.com/question/21318658  






<br/>
<br/>
http://www.zhihu.com/question/22608820
__这两门课程该如何学？看哪些书？__这里我告诉你一个通用的办法，去美国计算机系排名靠前的大学的课程主页，找到这两门课最近几年的课程大纲、讲义、参考书目、阅读材料、随堂练习、课后作业、编程实验、期末项目等，然后你就心里有数了。

__学习任何一门课程都要善于抓住主要矛盾、分清主次、突出重点，__关键是掌握知识框架，学会以后真正有用的知识和技能，而不要把精力平均分配在一些琐事上。


比如说操作系统，应该把精力主要放在进程管理与调度、内存管理、并发编程与同步、高效的IO等等，而不要过于投入到初始化（从 BIOS 加载引导扇区、设置 GDT、进入保护模式）这种一次性任务上。我发现国内讲 Linux 内核的书往往把初始化的细节放在前几章，而国外的书通常放附录，你可以体会一下。初始化对操作系统本身而言当然是重要的，但是对于在用户态写服务程序的人来说，弄清楚为什么要打开 PC 上的 A20 地址线真的有用处吗？（这不过是个历史包袱罢了。）

__注意分清知识的层次__。就好比造汽车与开汽车的区别，我认为一个司机的技能主要体现在各种道路条件和天气状况下都能安全驾驶（城市道路、高速公路、乡间公路 X 晴、雨、雪、雾），平安到达目的地。作为一名司机，了解汽车运行的基本原理当然是好事，可以有助于更好地驾驶和排除一些常见故障。但不宜喧宾夺主，只要你不真正从事汽车设计工作，你再怎么研究发动机、传动、转向，也不可能比汽车厂的工程师强，毕竟这是人家的全职工作。而且钻研汽车构造超过一定程度之后，对开好车就没多大影响了，成了个人兴趣爱好。“有的人学着学着成了语言专家，反而忘了自己原本是要解决问题来的。”（语出孟岩 快速掌握一个语言最常用的50%）

__如果你要记住结论，一定要同时记住前提和适用条件__。在错误的场合使用原本正确的结论的搞笑例子举不胜举。



<br/>
<br/>
### 面试题
6．PHP处理上传文件信息数组中的文件类型$_FILES['type']由客户端浏览器提供，有可能是黑客伪造的信息，请写一个函数来确保用户上传的图像文件类型真实可靠













<br/>
下面的题目来自: http://www.guokr.com/post/444387/  
[基础测试]

* 获取列表长度的函数
* 列表的排序函数
* 获取字典中某个键的值时，提供默认值
* 重载一个方法时的写法，注意继承父类方法的功能之上再扩展
* 按照ISO时间输出当前时间
* 调用ls命令并获取输出
* 识别IP地址的正则表达式
* GBK、UTF-8、Unicode三者的区别和联系
* TCP三次握手的包类型、TCP断开时的数据包个数和类型



[中级测试]

* 编写冒泡排序或其他排序方法
* 将一列元素存入列表，并使用二分查找法确认一个值所在列表中的位置区间，例如查找一个IP地址所在的IP段范围
* 编写一个类模拟字典的行为
* 仅使用socket模块编写一个多线程echo服务器
* 网络服务器的几种模式


[高级测试]

* 哈希表的实现原理中键碰撞后会导致查找性能降低，对Python大概在什么样的量级会开始出现该问题
* GIL的目的，绕开GIL使用多核的方法
* 标记-清除、引用计数等集中GC算法的优劣
* Python的几种并发实现方式的优劣：select()、twisted中的几种、stackless、greenlet、parallel python







<br/>
<br/>
### 推荐书籍 & 资料
1. 《 形形色色的科学-程序语言的奥妙：算法解读 》  
 
2. Axb的自我修养   
http://blog.2baxb.me/reading_list  

3. 啊哈算法  

4. 大话数据结构  


<br/>
<br/>
### 其他参考
wikipedia -- List of algorithms  
https://en.wikipedia.org/wiki/List_of_algorithms  



<br/>
<br/>
---
<br/>
#### 1. Ubuntu(14.04) 查看安装的 Python 版本
```
python -V
```
注意一定要大写的 V
小写 v 会被无视, 直接进入 Python


<br/>
<br/>
#### 安装最新的 Python 3.5
https://www.python.org/downloads/

解压 .xz 文件
tar xf Python-3.5.0.tar.xz

x
f





<br/>
<br/>
#### 装了2个版本的 Python 时, 要用 Python3 可以:
```
python3 7.InsertSort.py
```


<br/>
<br/>
#### rm -rf * - 删除当前目录下所有东西

rm - remove files or directories

-f  force, even this is a bad idea, just delete it, don't prompt
-r, -R, --recursive
              remove directories and their contents recursively




<br/>
<br/>
#### 总结
1. 深度优先搜索是一直往子节点下跑, 没有子节点了再上去, 再看看上面那一个有没有没访问过的子节点.  
2. 广度优先就是找邻居..  一层一层的找  

树的例子:  
文件系统  
族谱  
比赛晋级图  


二叉树 = 最多2个子节点, 一个左边一个右边. 允许只有左子节点或者只有右子节点, 并不是说除了叶节点之外其他节点都要有2个子节点才算  

<br/>
二叉树下面有两类: 满二叉树, 完全二叉树.

<br/>
满二叉树 = 全都有2个子节点, 深度一致  

<br/>
完全二叉树 = 全都有2个子节点, 深度不一致  

<br/>
堆是一种特殊的完全二叉树  
当一颗完全二叉树, 上级节点都比子节点小的时候, 叫做__最小堆__  
当一颗完全二叉树, 上级节点都比子节点大的时候, 叫做__最大堆__  

<br/>
堆有什么用?  
想从一堆数字里面找出最小的, 数组要遍历, 而最小堆直接拿根节点就是了  
假设现在要插入一个数字到堆里, 就根据大小, 从根节点开始, 向下比较, 找到合适的节点就插入成子节点就行了.

插入堆可以用__向上调整__或者__向下调整__  
向上调整和向下调整的区别是啥?  




<br/>
编译 C++ 程序要用 g++, 不能用 gcc  
```C++
g++ 2-Stack.cpp -o 2s
```






