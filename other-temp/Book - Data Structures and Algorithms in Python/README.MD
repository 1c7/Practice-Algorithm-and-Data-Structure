### Data Structures and Algorithms in Python







<br/>




第8章 树


第9章 优先队列-- Priority Queue

10  Maps, Hash Tables, and Skip Lists

11 Search Tree
120  sorting and sele

---

python 中 self 不是关键字
self 指的是类实例对象本身


---

你可以实现 class 的 next 方法把对象做成可迭代的，
也就是可以用 for in 这种的

---


网络中鉴别身份的方式：
	1.0 
	宣称自己是谁，然后别人就相信你了
	存在的问题：身份伪造太容易了

	2.0
	假设 Alice 有一个众所周知的 IP 地址
	那么可以：宣称自己是谁 + 自己的IP地址		
	存在的问题：IP 也是可以伪造的

	3.0 
	宣称自己是谁 + 口令
	问题：口令可以被拦截到

	3.1
	宣称自己是谁 + 加密之后的口令
	问题：无法防止"回放攻击"，人家拦截了加密后的口令之后再次发送就好了

	4.0
	3.1的问题是在于每次用的口令是一样的
	解决方案之一，是每次用不同的口令，约定一个口令生成算法
	这种解决方案还不够好
	我们可以用一个 nonce 不重数，就是一个只使用一次的数
	


























