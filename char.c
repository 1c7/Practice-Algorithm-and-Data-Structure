#include <stdio.h>
#include <string.h>
#define X 3
#include <limits.h>
#include <string.h>


int main(void){
  
  char c[5] = "aabb";
  const int X2 = 4;
  

  
  int o = 3; 
  int * p_o;  // 声明一个指针
  p_o = &o; // 取地址并且赋值给指针
  *p_o = 123; // 根据地址赋值
  
  
  char infinite[] = "ppplllzzz999";
  // how this work?
  
  char infi_len = strlen(infinite);
  
  char * infi = "9999999999";
  
  
  
  printf("%s\n", c); // 字符串
  printf("%d\n", X); // 常量1
  printf("%d\n", X2); // 常量2
  printf("%d\n", *p_o); // 指针
  printf("%p\n", p_o); // 指针地址
  printf("%s\n", infinite); // 变长字符串
  printf("%s\n", infi); // 变长字符串
  printf("%d\n", infi_len); // 变长字符串
  
  
  return 0;
}















