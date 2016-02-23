package week2;

import java.util.Iterator;

/**
 * Generics 实现栈 .  Generics 叫泛型
 *
 * 用 Generics 的理由:
 * 拿之前的栈举例, 假设我们要的栈不是用来存字符串, 用来存别的对象呢?
 * 在写一个? 复制粘贴? 太麻烦了
 * 
 * 照着视频打的，这个是链表栈的 Generics 写法
 * 数组栈的没写
 *
 */
public class GenericsLinkedStack<Item> implements Iterable<Item>{ // 注意这里的 Item
	private Node first = null;
	
	private class Node{
		Item item;     // 注意这里
		Node next;
	}
	
	public boolean isEmpty(){
		return first == null;
	}
	
	public void push(Item item){ // 注意这里
		Node oldFirst = first;
		first = new Node();
		first.item = item;
		first.next = oldFirst;
	}
	
	public Item pop(){          // 注意这里
		Item item = first.item; // 注意这里
		first = first.next;
		return item;
	}

	@Override
	public Iterator<Item> iterator() {
		return new ListIterator();
	}
	
	private class ListIterator implements Iterable<Item>{
		
		private Node current = first;
		
		public boolean hasNext(){
			
			return current != null;
		}
		public void remove(){
			// not support
		}
		public Item next(){
			Item item = current.item;
			current = current.next;
			return item;
		}
	}
	
}


