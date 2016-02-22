package week1;

/*
 * 写给正在读代码的你:
 * 
 * 代码是基于 Coursera 课程  Algorithem Part 1 写的
 * 不建议单独看代码, 搭配视频看更好
 * 
 * 第  1 周描述的问题是   如何判断  2 个点是否连接在一起?
 * 
 * 思路1:  QuickFind
 *   如名字所暗示的, find 操作很快, 也就是判断2个点是否连接很快
 *   但是 union 很慢.
 *   
 *   实现方法: 用一个数字数组, 索引代表点, 如果值一样代表连接在一起了
 *   union 操作因为要改很多值导致很慢
 * 
 * 思路2:  QuickUnion
 *   union 操作快, find 操作慢
 *   实现方法: 用了 tree 这种思路, 索引代表点, 值代表上级元素的索引
 *   union 操作只需要改一个值就行了
 *   但当问题大了之后, tree 会很高, 导致 find 操作很慢
 *   
 * 
 * */
public class Main {
	public static void main(String[] args){
		//int N = StdIn.r
		System.out.println("123");
	}
}































