#include <stdio.h>
#include <stdlib.h>
// for exit() function


int main(void){
  
  FILE *f = fopen("file.txt", "w");
  if (f == NULL)
  {
      printf("Error opening file!\n");
      exit(0);
  }

  /* print some text */
  const char *text = "Write this to the file";
  fprintf(f, "Some text: %s\n", text);
  // fprintf 输出到文件里
  // 第一个参数是文件指针, 第二第三个是字符串和占位
  
  /* print integers and floats */
  int i = 1;
  float py = 3.1415927;
  fprintf(f, "Integer: %d, float: %f\n", i, py);

  /* printing single chatacters */
  char c = 'A';
  fprintf(f, "A character: %c\n", c);

  fclose(f);

  return 0;
}
/*

  文件指针 = fopen(文件地址, 打开模式)
  
  
  
  

*/














