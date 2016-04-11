package week1;


/* Quick Find ���ֽ��������
 * ��һ��������������ʾ�㣬�Լ���֮�������
 * 
 * �������������"��"
 * �����ֵ���һ��, ��������"��"������һ����
 * 
 * ���ֽ���������������� Union ������Ҳ��������2����Ĳ������ڷ�ʱ
 * Ҫ������������ȥ�滻ֵ
 * */
public class QuickFind {
	
	private int[] id;
	
	// ��ʼ��
	// �����ʼ��ʹ�������"����"��"ֵ"һ��
	public QuickFind(int N){
		id = new int[N];
		for (int i=0; i< N; i++){
			id[i] = i;
		}
	}
	
	// �������Ƿ�������һ��
	public boolean connected(int p, int q){
		return id[p] == id[q];
	}
	
	// ����2����(��ֵ�ĳ�һ��)
	public void union(int p, int q){
		int pid = id[p];
		int qid = id[q];
		// ������������ֵ
		for(int i=0; i<id.length; i++){
			if (id[i] == pid) id[i] = qid;
		}
	}
	

}




















