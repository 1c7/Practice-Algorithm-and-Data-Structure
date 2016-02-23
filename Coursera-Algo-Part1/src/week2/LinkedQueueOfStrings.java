package week2;



/**
 * 链表实现队列
 * 需要 mantain two pointer, 一个是指向头部, 一个是指向尾部
 * 
 */
public class LinkedQueueOfStrings {
	
	private Node first, last;

	private class Node{
		String item;
		Node next;
	}
	
	// 入队
	public void enqueue(String item){
		Node oldLast = last; // 先把最后一个节点存起来
		Node newNode = new Node();
		newNode.item = item; 
		newNode.next = null; 
		if (isEmpty()){
			first = newNode; // 如果是空队列, 那么新的这个节点就是 first 节点
		}
		else{
			oldLast.next = newNode; // 如果队列不为空, 那么新节点会在最后一个节点后面
		}
	}
	
	// 出队
	public String dequeue(){
		String item = first.item; // 先拿到第一个元素的内容
		first = first.next; // 去掉第一个元素
		if(isEmpty()){
			last = null;
		}
		return item;
	}
	
	boolean isEmpty(){
		return first == null;
	}
	
}








