package week2;

/**
 * ������ʵ��ջ
 *
 */
public class LinkedStackOfStrings {
	
	private Node first = null;
	
	private class Node{
		String item;
		Node next;
	}
	
	public boolean isEmpty(){
		return first == null;
	}
	
	public void push(String item){
		Node oldFirst = first;
		first = new Node();
		first.item = item;
		first.next = oldFirst;
		// ���½ڵ�� next ָ�� �Ͻڵ�
	}
	
	public String pop(){
		String item  = first.item; // �õ���1���ڵ��ֵ
		first = first.next; // pop ������
		return item; // ���ص�1���ڵ��ֵ
	}
	
	
	
}












