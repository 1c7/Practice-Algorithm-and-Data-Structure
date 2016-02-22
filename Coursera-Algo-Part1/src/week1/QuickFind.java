package week1;


/* Quick Find 这种解决方法是
 * 用一个数字数组来表示点，以及点之间的连接
 * 
 * 数组的索引代表"点"
 * 数组的值如果一样, 代表两个"点"连接在一起了
 * 
 * 这种解决方法的问题在于 Union 操作，也就是连接2个点的操作过于费时
 * 要遍历整个数组去替换值
 * */
public class QuickFind {
	
	private int[] id;
	
	// 初始化
	// 这个初始化使得数组的"索引"和"值"一样
	public QuickFind(int N){
		id = new int[N];
		for (int i=0; i< N; i++){
			id[i] = i;
		}
	}
	
	// 两个点是否连接在一起
	public boolean connected(int p, int q){
		return id[p] == id[q];
	}
	
	// 连接2个点(把值改成一样)
	public void union(int p, int q){
		int pid = id[p];
		int qid = id[q];
		// 遍历数组来改值
		for(int i=0; i<id.length; i++){
			if (id[i] == pid) id[i] = qid;
		}
	}
	

}




















