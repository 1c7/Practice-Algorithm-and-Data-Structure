package week2;



/**
 * ����ʵ�ֶ���
 * ��Ҫ mantain two pointer, һ����ָ��ͷ��, һ����ָ��β��
 * 
 */
public class LinkedQueueOfStrings {
	
	private Node first, last;

	private class Node{
		String item;
		Node next;
	}
	
	// ���
	public void enqueue(String item){
		Node oldLast = last; // �Ȱ����һ���ڵ������
		Node newNode = new Node();
		newNode.item = item; 
		newNode.next = null; 
		if (isEmpty()){
			first = newNode; // ����ǿն���, ��ô�µ�����ڵ���� first �ڵ�
		}
		else{
			oldLast.next = newNode; // ������в�Ϊ��, ��ô�½ڵ�������һ���ڵ����
		}
	}
	
	// ����
	public String dequeue(){
		String item = first.item; // ���õ���һ��Ԫ�ص�����
		first = first.next; // ȥ����һ��Ԫ��
		if(isEmpty()){
			last = null;
		}
		return item;
	}
	
	boolean isEmpty(){
		return first == null;
	}
	
}








