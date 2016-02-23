package week2;

import java.util.Iterator;

/**
 * Generics ʵ��ջ .  Generics �з���
 *
 * �� Generics ������:
 * ��֮ǰ��ջ����, ��������Ҫ��ջ�����������ַ���, �������Ķ�����?
 * ��дһ��? ����ճ��? ̫�鷳��
 * 
 * ������Ƶ��ģ����������ջ�� Generics д��
 * ����ջ��ûд
 *
 */
public class GenericsLinkedStack<Item> implements Iterable<Item>{ // ע������� Item
	private Node first = null;
	
	private class Node{
		Item item;     // ע������
		Node next;
	}
	
	public boolean isEmpty(){
		return first == null;
	}
	
	public void push(Item item){ // ע������
		Node oldFirst = first;
		first = new Node();
		first.item = item;
		first.next = oldFirst;
	}
	
	public Item pop(){          // ע������
		Item item = first.item; // ע������
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


