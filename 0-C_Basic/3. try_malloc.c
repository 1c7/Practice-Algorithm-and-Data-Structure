#include <stdio.h>
#include <stdlib.h>
// for malloc() free()


int main(void){
  
  int * x = malloc(8 * sizeof(int));
  *x = 123456;
  
  
  printf("%d\n", *x);
  
  return 0;
}















