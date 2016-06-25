#include <cstdio>
#include <iostream>       // std::cout
#include <stack>          // std::stack

using namespace std;

// <挑战程序设计竞赛> 第28页
// 记得要用 g++ 而不是 gcc
// pop 只是移除顶端元素, 要获得顶端元素用 top

int main(){
  stack<int> s; // 声明存储 int 类型的栈
  s.push(1);
  s.push(2);
  s.push(3);
  
  printf("%d\n", s.top());
  cout << "number is " << s.top() << endl;

  s.pop();
  printf("%d\n", s.top());
  cout << "number is " << s.top() << endl;
   
   
  return 0;
}








