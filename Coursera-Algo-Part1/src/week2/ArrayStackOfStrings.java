package week2;

/**
 * ��������ʵ��ջ
 * ����˼·����һ���ַ�������, ���һ��������������¼�ж��ٸ�Ԫ��.
 * overhead ����
 * 
 * ���ּ������������������̶�.
 * 
 * 
 * ����ʱ����������ô��?
	 * First try:
	 * push ��ʱ�� array size +1
	 * pop ʱ array size -1
	 * 
	 * �����������ֲ���̫ expensive ��
	 * Ҫ�����������ֲ���
	 * ����������ÿ�ζ� double size array������ֱ�ӱ�����
	 * (�뿴 push �������ʵ��)
 * 
 * 
 * ��Ҫ��������ʱ��ô��? (����ܶ� pop ����)
	 * First try:
	 * ��Ȼ����֮ǰ�������������������˾� double ����
	 * ��ô pop ��ʱ���������������һ��, ����������?
	 * ȱ��: �������������һ��ͼ���, �ᵼ�¼���֮��պ���������. �ٴ� push ������Ҫ double ����.
	 * ���һֱ  push,pop,push,pop
	 * �ͻᵼ�����ܺܲ�, ��Ϊһ�� double ����, һ�� halve ����
	 * 
	 * �������: ��  pop ֮��������ֻ�����ķ�֮һ, �� halve ����
	 * (�뿴 pop �������ʵ��)
 * 
 * 
 */
public class ArrayStackOfStrings {
	private String[] s;
	private int N = 0; // ��¼�ж��ٸ�Ԫ��
	
	// ��ʼ���ַ�������
	public ArrayStackOfStrings(){
		s = new String[1];
	}
	
	public boolean isEmpty(){
		return N == 0;
	}
	
	public void push(String item){
		if (N == s.length){
			resize(2 * s.length);
		}
		s[N++] = item;
	}
	
	// ʵ�ʾ��ǽ���������, Ȼ����ϵ�ȫ�� copy ��ȥ
	private void resize(int capacity){
		String[] copy = new String[capacity];
		for (int i=0; i<N; i++){
			copy[i] = s[i];
		}
		s = copy;
	}
	
	public String pop(){
		String item = s[--N];
		s[N] = null;  // ��� null ��Ϊ�˸���Ч���ڴ�, ��������þ�˵������ pointer ָ������.(��Ƶ˵��)
		if (N>0 && N == s.length/4){
			resize(s.length/2);
		}
		return item;
	}
	
}














