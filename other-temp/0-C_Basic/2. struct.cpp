#include <stdio.h>
#define MAXTITLE 41
#define MAXAUTHOR 33

// 结构
struct book{
  char title[MAXTITLE];
  char author[MAXAUTHOR];
  float value;
};

// 联合 union
union hold{
  int digit;
  double flo;
  char letter;
};


enum a {aa,bb,cc,dd};


struct film{
  char title[54];
  int rating;
  struct film * next;
}



int main(void){

  struct book libary = {
    "haha title",
    "handsome jack",
    39.95
  };

  printf("%s\n", libary.title);



  union hold fit;
  union hold save[10];
  union hold * pu;

  

  fit.digit = 23;
  fit.flo = 99.921233333333333333;

  printf("%d\n", fit.digit);
  printf("%f\n", fit.flo);
  
  
  
  // enum
  
  
  
  printf("%f\n", a);
  

}







