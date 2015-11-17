

'''
Data Structures and Algorithms in Python

    p211~214

一个有排名的游戏积分榜

Scoreboard 是积分榜
Scoreboard 里面存的是 GameEntry
GameEntry 存的是人名和对应的积分

'''




class GameEntry:

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)

'''
a = GameEntry("James Bond", '7')

print(a.get_name())
print(a.get_score())
print(a)
'''

class Scoreboard:

    def __init__(self, capacity=10):
        self._board = [None] * capacity
        self._n = 0
        # n 是存积分榜里存了多少个元素

    def __getitem__(self, k):
        return self._board[k]
    # ..


    def __str__(self):
        return '\n'.join(str(self._board[j]) for j in range(self._n))
    # print(对象)的时候会调用到 __str__


    def add(self, entry):
        score = entry.get_score()
        # 拿到分数

        # 这个新元素有资格进入积分榜吗？
        # 1. 积分榜没满，
        # 2. 积分榜满了但是这个新加入的分数比最低分要高
        good = self._n < len(self._board) or score > self._board[-1].get_score()
        
        if good:
            # 如果情况是积分榜没满
            if self._n < len(self._board):
                self._n += 1
            
            j = self._n - 1
            # 没插入新元素前，最后一个元素的索引
            
            while j > 0 and self._board[j-1].get_score() < score:
                # 如果最后一个元素比要插入的新元素的分数低
                # 
                
                self._board[j] = self._board[j-1]
                # 把前一个元素盖掉后一个元素
                
                j -= 1

                # 重复这个过程(while) 直到找到合适的位置

            self._board[j] = entry
            # 插入新元素
    


PlayerA = GameEntry("Jame", 17)
PlayerB = GameEntry("Celine", 28)
PlayerC = GameEntry("Cherry", 39)
PlayerD = GameEntry("Bob", 1)
PlayerE = GameEntry("Kutchy", 127)
PlayerF = GameEntry("Blue", 228)
PlayerG = GameEntry("Ben", 11)
PlayerH = GameEntry("Jack", 28)



board = Scoreboard()
board.add(PlayerA)
board.add(PlayerB)
board.add(PlayerC)
board.add(PlayerD)
board.add(PlayerE)
board.add(PlayerF)
board.add(PlayerG)
board.add(PlayerH)


print(board)






























