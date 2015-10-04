#include <stdio.h>

void main(void){
   int a[6] = {9, 2, 3, 8, 4, 6};
   int i; // for loop 
   int t; // for temporary
   int j;
   int smallest = a[0];
   
   
   
  printf("--Start Selection Bubble Sort\n");
  
  // ==== output unsorted array ====
  for(i=0; i<6; i++){
    printf("%d", i);
    printf("    %d\n",a[i]);
  }
  printf("\n");
  // ==== end ====
   
   
   for(i=0; i<6; i++){
    for(j=i; j<6; j++){
    
      if(a[i] < smallest){
        t = smallest;
        smallest = a[i];
        a[i] = t;
      }
      
    }
   }


  for(i=0; i<6; i++){
    printf("%d", i);
    printf("    %d\n",a[i]);
  }
  printf("\n");



}
