package week1;


/*
 * QuickUnion ���ֽ������
 * �ṹ�Ϻ� QuickFind һ�£��õ���һ����������
 * ����ֵ������ϼ�Ԫ�ص�����
 * 
 * Quick Find ��ֵ���һ������Ϊ����������һ��
 * Quick Union ��ֵ������ϼ�Ԫ�ص�����
 * 
 * ���һ��Ԫ��û���ϼ�, ��ô index ��  value һ��
 * 
 * 
 * Find: ��������Ԫ���Ƿ��� same root
 * 
 * Union: �� q ���Ǹ���Ԫ��, ָ�� p �ĸ�Ԫ��
 * Ҳ���ǰ� q �ĸ�Ԫ�ص�ֵ, �ĳ� p �ĸ�Ԫ�ص�����
 * ���߷�����Ҳ��, ��һ��Ҫ�� q
 * 
 * ��� Union �����ͺܼ���, ֻ�� Find �����鷳�� 
 * 
 * */
public class QuickUnion {
	
	private int[] id;
	
	// ��ʼ��
	// �� QuickFind һ����
	public QuickUnion(int N){
		id = new int[N];
		for (int i=0; i< N; i++){
			id[i] = i;
		}
	}
	
	private int root(int i){
		while(i != id[i]) i = id[i];
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
		id[i] = j;
		// �õ���Ԫ�ص�ֵ
		// ������һ��Ԫ��ָ����һ����Ԫ��
	}
	
}



































