#include <stdio.h>
int a[101];

// 还不能用.

// 输入: 
// 输出: 
void QuickSort(int left, int right){
  
  printf("start quick sort\n");
  printf("--left is %d\n", left);
  printf("--right is %d\n", right);
  
  
  int i; // 
  int j; // 
  int t; // 用于交换元素时的临时存储.
  int temp; // 存基准数
  
  
  // 
  if(left > right){
    return;
  }
  
  temp = a[left]; // 基准数
  i = left;
  j = right;
  
  while(i!=j){
    printf("get in FIRST while\n");
    
    while(a[j] >= temp && i<j){
      j--; 
      // 从右边往左找
      // 直到找到一个比 基准数字 小的元素, while 就跳出了
      // j 同时不能越过 i
    }
    
    while(a[j] <= temp && i<j){
      i++;
    }
    
    if(i<j){
      printf("----switch position\n");
      t = a[i];
      a[i] = a[j];
      a[j] = t;
    }
  
  }// while end
  
  // 运行到这里代表 i == j 了
  // 那么就将 基准数 放到 i 和 j 重合这个位置
  // 还记得前面我们把 基准数 放到 temp 里了吗?
  // 现在 a[i] 是重合位置的元素
  // temp 是基准数
  a[left] = a[i];
  a[i] = temp;
   
  
  // 递归处理左半边和右半边
  QuickSort(left, i-1); 
  QuickSort(i+1, right);
  
}


void main(){

  int a[6] = {12, 8, 1, 3, 6, 2};
  
  int len = (int)( sizeof(a) / sizeof(a[0]) );
  // get array length
  // http://stackoverflow.com/questions/37538/how-do-i-determine-the-size-of-my-array-in-c
  
  int i; // 用于循环
  
  
  // ------- 开始服药治疗 -------
  printf("array length == %d\n", len);
  
  
  // 排序前
  for(i=0; i<len; i++){
    printf("%d\n", a[i]);
  }
  printf("-------------------\n");
  
  
  
  
  QuickSort(0, len);
  
  
  
  
  // 排序后
  printf("-------------------\n");
  for(i=0; i<len; i++){
    printf("%d\n", a[i]);
  }
  
  
  
}











