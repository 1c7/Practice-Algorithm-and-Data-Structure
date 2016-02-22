package week1;


/*
 * QuickUnion 这种解决方法
 * 结构上和 QuickFind 一致，用的是一个整数数组
 * 但是值存的是上级元素的索引
 * 
 * Quick Find 是值存的一样就认为是连接在了一起
 * Quick Union 的值存的是上级元素的索引
 * 
 * 如果一个元素没有上级, 那么 index 和  value 一样
 * 
 * 
 * Find: 看看两个元素是否有 same root
 * 
 * Union: 把 q 的那个根元素, 指向 p 的根元素
 * 也就是把 q 的根元素的值, 改成 p 的根元素的索引
 * 或者反过来也行, 不一定要是 q
 * 
 * 这次 Union 操作就很简单了, 只是 Find 操作麻烦点 
 * 
 * */
public class QuickUnion {
	
	private int[] id;
	
	// 初始化
	// 和 QuickFind 一样的
	public QuickUnion(int N){
		id = new int[N];
		for (int i=0; i< N; i++){
			id[i] = i;
		}
	}
	
	private int root(int i){
		while(i != id[i]) i = id[i];
		// 如果 index 和 value 不一样代表没到 root
		// 到了 root 就一样了. 就返回  value 就好
		return i;
	}
	
	public boolean connected(int q, int p){
		return root(p) == root(q);
	}
	
	public void union(int q, int p){
		int i = root(p);
		int j = root(q);
		id[i] = j;
		// 拿到根元素的值
		// 把其中一个元素指向另一个根元素
	}
	
}



































