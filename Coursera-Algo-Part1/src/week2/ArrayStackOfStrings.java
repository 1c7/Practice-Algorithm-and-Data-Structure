package week2;

/**
 * 用数组来实现栈
 * 总体思路就是一个字符串数组, 外加一个整数变量来记录有多少个元素.
 * overhead 开销
 * 
 * 这种简单做法的问题是容量固定.
 * 
 * 
 * 插入时超出容量怎么办?
	 * First try:
	 * push 的时候 array size +1
	 * pop 时 array size -1
	 * 
	 * 但问题是这种操作太 expensive 了
	 * 要尽量减少这种操作
	 * 所以做法是每次都 double size array，容量直接变两倍
	 * (请看 push 方法里的实现)
 * 
 * 
 * 需要减少容量时怎么办? (比如很多 pop 操作)
	 * First try:
	 * 既然我们之前增加容量的做法是满了就 double 容量
	 * 那么 pop 的时候如果到了容量的一半, 就容量减半?
	 * 缺点: 如果到了容量的一半就减半, 会导致减半之后刚好满了容量. 再次 push 就又需要 double 容量.
	 * 如果一直  push,pop,push,pop
	 * 就会导致性能很差, 因为一会 double 容量, 一会 halve 容量
	 * 
	 * 解决方法: 当  pop 之后发现容量只用了四分之一, 就 halve 容量
	 * (请看 pop 方法里的实现)
 * 
 * 
 */
public class ArrayStackOfStrings {
	private String[] s;
	private int N = 0; // 记录有多少个元素
	
	// 初始化字符串数组
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
	
	// 实际就是建个新数组, 然后把老的全部 copy 进去
	private void resize(int capacity){
		String[] copy = new String[capacity];
		for (int i=0; i<N; i++){
			copy[i] = s[i];
		}
		s = copy;
	}
	
	public String pop(){
		String item = s[--N];
		s[N] = null;  // 设成 null 是为了更高效用内存, 如果不设置据说还会有 pointer 指向那里.(视频说的)
		if (N>0 && N == s.length/4){
			resize(s.length/2);
		}
		return item;
	}
	
}














