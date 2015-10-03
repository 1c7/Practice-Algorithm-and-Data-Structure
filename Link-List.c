#include <stdio.h>
#include <stdlib.h>


/*
  malloc 函数的返回类型是 void * 类型
  需要转换成对应的类型  
  
  指针为什么需要类型?
  
  指针变量存的是第一个地址
，为什么要分不同类型的指针呢？因为指针
变量存储的是一个内存空间的首地址（第一个字节的地址），但是这个空间占用了多少个字
节，用来存储什么类型的数，则是由指针的类型来标明的。这样系统才知道应该取多少个连
续内存作为一个数据。

*/




// 链表  <啊哈 算法> 第63是最后一页(有关链表的)


struct node{
  int data;
  struct node * next;

};






void main(){

  struct node * head;
  head = NULL;

  struct node * p;
  p=(struct node *)malloc(sizeof(struct node));
  
  p->data=a;//将数据存储到当前结点的data域中
  p->next=NULL;//设置当前结点的后继指针指向空，也就是当前结点的下一个结点为空
  
  
  
  
  
  
  
  
}









