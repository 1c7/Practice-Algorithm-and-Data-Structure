package week2;

/**
 * 链表来实现栈
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
		// 把新节点的 next 指向 老节点
	}
	
	public String pop(){
		String item  = first.item; // 拿到第1个节点的值
		first = first.next; // pop 操作了
		return item; // 返回第1个节点的值
	}
	
	
	
}












