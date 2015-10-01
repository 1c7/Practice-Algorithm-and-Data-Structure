#include <stdio.h>
 

// 冒泡排序
void main(){

  int a[8] = {12, 99, 21, 1, 8 ,3, 888, 66};
  int i,j;  // used in loop
  int t = 0;    // used for temporary store number
  
  
  printf("Length of array: %d\n", (int)( sizeof(a) / sizeof(a[0]) ));
  // get array length
  // http://stackoverflow.com/questions/37538/how-do-i-determine-the-size-of-my-array-in-c
  
  int len = (int)( sizeof(a) / sizeof(a[0]) );
  
  
  
  
  // for 循环一次只能将一个数字归位
  // 数组有多少n个元素,就要循环n-1次
  // 我们把最大的放最后
  // 假设5个元素
  // 第一次循环, 比较 1~5, 就是说 1:2 2:3 3:4 4:5 
  //  现在第5个元素是最大的了
  // 第二次循环, 比较 1-4
  // 第三次循环, 比较 1-3
  // 第四次循环, 比较 1-2
  // 收工
  
  printf("--Start Running Bubble Sort\n");
  
  // ==== output unsorted array ====
  for(i=0; i<len; i++){
    printf("%d", i);
    printf("    %d\n",a[i]);
  }
  printf("\n");
  // ==== end ====
  

  for(i=1; i<len; i++){ 
  // 必须是1 到 数组长度-1 因为里面那个循环要用到这个数去减
    printf("%d---", i);
    for(j=0; j<len-i; j++){  // 0 到 数组长度-上层循环的数字 
    
      printf("%d:", j);
      printf("%d", j+1);
      printf(" ");
      
      if(a[j] > a[j+1]){ 
      // 如果 > 后面那个元素, 就互换, 这样大的元素就换到后面去了.
        t = a[j];
        a[j] = a[j+1];
        a[j+1] = t;
      }
      
    }
    printf("\n");
  }
  
  
  // ==== output result ====
  printf("\n");
  printf("--Sort done\n");
  for(i=0; i<len; i++){
    printf("%d", i);
    printf("    %d\n",a[i]);
  }
  // ==== end ====





/*
  重点总结:
    冒泡排序需要2个循环嵌套
    第一个循环是 1到数组长度-1
    第二个循环是 0到数组长度-上一个循环的值
    
    比如6个元素
    第一个循环是 1到5  也就是要进行5趟,每一趟归位一个元素到最后
    第二个循环是的数字要用到数组下标里,所以要从0开始
    6个元素的下标是 0~5
    第一趟  比较0~5 
    第二趟  比较0~4
    第三趟  比较0~3
    第四趟  比较0~2
    第五趟  比较0和1

    6个元素一共要比较多少次?
    第1趟 5次
    2 4次
    3 3次
    4 2次
    5 1次
    
    6个元素,要比较的次数等于 5+4+3+2+1 = 15次
    
    在最糟糕情况下, 每次比较都要交换, 比较和交换的次数都加上,等于
    1 5次+5 = 10
    2 4次   = 8
    3 3次  = 6
    4 2次  = 4
    5 1次  = 2
    10+8+6+4+2 = 18+6+4+2 = 28+2 = 30

    
    6个元素, 最糟情况比较加交换30次
    6 -> 30
    
    6-1 = 5
    5+5 + 4+4 + 3+3 + 2+2 + 1+1
    


    ===================================
    
    
    等差数列 - arithmetic progression
    https://zh.wikipedia.org/wiki/%E7%AD%89%E5%B7%AE%E6%95%B0%E5%88%97
    
    等差数列求和 : (第一项+第n项) * n / 2
    (1 + 5) * 5 / 2 
      = 30 / 2 
      = 15
    
    (1+100)*100/2
      = 10100 / 2
      = 5050
      
   =======================================
      
    既然大家都说冒泡排序的时间复杂度 O(n^2)
    n的平方
    

      
    
*/

  int seq, number, result = 0;
  
  printf("\n");
  for(seq=2; seq<10; seq++){
    printf("%d个元素 ", seq);
    for(number=1; number<=seq-1; number++){
      result = result + number + number;
    }
    printf("最糟情况比较和交换一共%d次", result);
    printf("---%d的平方是%d", seq, (seq)*(seq));
    printf("---平方减次数=%d", (seq)*(seq)-result);
    printf("\n");
    result = 0;
  }





} // main end










