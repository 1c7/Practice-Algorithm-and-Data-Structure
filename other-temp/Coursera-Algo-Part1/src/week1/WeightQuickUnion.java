package week1;

/*
 * 改进 Quick Union
 * 主要点是不要让 tree 那么高(层级少)
 * 方法是 union 的时候把小树挂在大树上
 * 
 * Data Structure 和 QuickUnion 一样，
 * 只不过这次多了一个 sz[i] 数组
 * 用来存 tree 有多少个元素
 * 
 * 第二个  improve 依然是减少树的高度
 * 这次的做法是 union 两个 tree 的时候，
 * 直接指向根元素就好， 
 * 而不是向以前一样指向另外一个 tree 里面的元素
 * 
 * */
public class WeightQuickUnion {
	
	private int[] id;
	private int[] sz;
	
	public WeightQuickUnion(int N){
		id = new int[N];
		sz = new int[N];
		for (int i=0; i< N; i++){
			id[i] = i;
		}
	}
	
	private int root(int i){
		while(i != id[i]){
			id[i] = id[id[i]];
			i = id[i];
		}
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

		if (i == j) return;
		// 如果根元素一致就没有必要 union 了, 直接 return 
		
		// 下面这段也就是看哪个小, 就挂在另一个大一点的上面.
		if (sz[i] < sz[j]){
			id[i] = j;
			sz[j] += sz[i];
		} else {
			id[j] = i;
			sz[i] += sz[j];
		}
	}
	
	
}










