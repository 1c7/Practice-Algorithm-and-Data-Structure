## Round 1A 2008
### Problem B. Milkshakes
奶昔  
问题描述真的好长啊  
看了半天才明白什么意思  


## 后记总结
这题我折腾了一个下午（当然我经常分心看视频玩去了所以实际也没那么久）  
写了无数屎一样的代码，堆了一堆 if else 看着都晕  
写了些能过 example 但是过不了实际例子的代码  
实在没办法了，只能去搜别人怎么解题的  


在这里 https://www.go-hero.net/jam/08/solutions/1/2/Python  
下载了一些代码，但是发现都是 python2.5 之类的(2008年嘛，可以理解)，我本地一运行就停住了。。
懒得调错，不管了  


注意重点是顾客最多有一个 melt, 这个大大简化了问题  

在网上看到一篇文  
https://bjlee72.wordpress.com/2014/08/18/google-code-jam-round-1a-2008-milkshake/  
哈哈哈，这个家伙花了9个小时，  
原来不止我一个人这么搓啊  










```


You own a milkshake shop. There are N different flavors that you can prepare, and each flavor can be prepared "malted" or "unmalted". So, you can make 2N different types of milkshakes.

你有个奶昔店
N种不同口味
每种口味可以预先准备成 malted 或者 unmalted
所以你一共可以有2N种奶昔

Each of your customers has a set of milkshake types that they like, and they will be satisfied if you have at least one of those types prepared. At most one of the types a customer likes will be a "malted" flavor.
你的每个客户都有一组喜欢的口味类型，如果至少有1个满足，他们就满意了。
客户喜欢的类型里，最多只有一种是 malted 的

You want to make N batches of milkshakes, so that:
你想制作 N 批奶昔，满足：


	* There is exactly one batch for each flavor of milkshake, and it is either malted or unmalted.
	* For each customer, you make at least one milkshake type that they like.
	* The minimum possible number of batches are malted.



Find whether it is possible to satisfy all your customers given these constraints, and if it is, what milkshake types you should make.
If it is possible to satisfy all your customers, there will be only one answer which minimizes the number of malted batches.
弄清是否可能满足你的顾客，如果可以，你应该制作什么类型的奶昔？
如果可以满足所有顾客，那么只有一种解法。




Input

	* One line containing an integer C, the number of test cases in the input file.

For each test case, there will be:
	* One line containing the integer N, the number of milkshake flavors.
	* One line containing the integer M, the number of customers.
	* M lines, one for each customer, each containing:
	* 
		* An integer T >= 1, the number of milkshake types the customer likes, followed by
		* T pairs of integers "X Y", one for each type the customer likes, where X is the milkshake flavor between 1 and N inclusive, and Y is either 0 to indicate unmalted, or 1 to indicated malted. Note that:
		* 
			* No pair will occur more than once for a single customer.
			* Each customer will have at least one flavor that they like (T >= 1).
			* Each customer will like at most one malted flavor. (At most one pair for each customer has Y = 1).


	* All of these numbers are separated by single spaces.


第一行是 test case

然后是 N，奶昔的口味数量
然后是 M，顾客数量
M 行，每行代表一个顾客
每行包含了：
     一个整数 T >= 1 ，代表着顾客喜欢多少种类型，
     然后是：T 对数字 X Y ，每一对都是顾客喜欢的类型
     X 是口味，1~N，   Y 是 0 代表 unmalted，1 代表 malted
          注意：
               一个顾客不会重复有 pair
               每个顾客至少喜欢一种口味，T >=1
               每个顾客最多一种 malted flavor，     


Output


	* C lines, one for each test case in the order they occur in the input file, each containing the string "Case #X: " where X is the number of the test case, starting from 1, followed by:
	* 
		* The string "IMPOSSIBLE", if the customers' preferences cannot be satisfied; OR
		* N space-separated integers, one for each flavor from 1 to N, which are 0 if the corresponding flavor should be prepared unmalted, and 1 if it should be malted.



输出
     C行
     case
          如果无法满足就  IMPOSSIBLE
          N 个空格间隔的数字，数字是1~N代表着口味，
          

```



### 









