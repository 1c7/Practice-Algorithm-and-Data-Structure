#include <cstdio>
#include <iostream>       // std::cout
#include <stack>          // std::stack

using namespace std;

// <挑战程序设计竞赛> 第28页
// 跑不起来, 叹..

int main(){
  stack<int> s; // 声明存储 int 类型的栈
  s.push(1);
  s.push(2);
  s.push(3);
  //printf("%d\n", s.top());

  s.pop();
  //printf("%d\n", s.top());

  return 0;
}








