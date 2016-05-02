package week1;

/*
 * �Ľ� Quick Union
 * ��Ҫ���ǲ�Ҫ�� tree ��ô��(�㼶��)
 * ������ union ��ʱ���С�����ڴ�����
 * 
 * Data Structure �� QuickUnion һ����
 * ֻ������ζ���һ�� sz[i] ����
 * ������ tree �ж��ٸ�Ԫ��
 * 
 * �ڶ���  improve ��Ȼ�Ǽ������ĸ߶�
 * ��ε������� union ���� tree ��ʱ��
 * ֱ��ָ���Ԫ�ؾͺã� 
 * ����������ǰһ��ָ������һ�� tree �����Ԫ��
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
		// ��� index �� value ��һ������û�� root
		// ���� root ��һ����. �ͷ���  value �ͺ�
		return i;
	}
	
	public boolean connected(int q, int p){
		return root(p) == root(q);
	}
	
	public void union(int q, int p){
		int i = root(p);
		int j = root(q);

		if (i == j) return;
		// �����Ԫ��һ�¾�û�б�Ҫ union ��, ֱ�� return 
		
		// �������Ҳ���ǿ��ĸ�С, �͹�����һ����һ�������.
		if (sz[i] < sz[j]){
			id[i] = j;
			sz[j] += sz[i];
		} else {
			id[j] = i;
			sz[i] += sz[j];
		}
	}
	
	
}










