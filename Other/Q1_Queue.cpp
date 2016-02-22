#include <cstdio>
#include <queue>
#include <iostream>       // std::cout


// g++ Q1_Queue.cpp -o q1

using namespace std;

// 队列是先入先出

int main(){
  queue<int> q;
  q.push(1);
  q.push(2);
  q.push(3);

  cout << "Queue number is " << q.front() << endl;
  // 输出队头

  q.pop(); // 扔掉队头

  cout << "Queue number is " << q.front() << endl;
  // 再输出一次队头

  return 0;
}

