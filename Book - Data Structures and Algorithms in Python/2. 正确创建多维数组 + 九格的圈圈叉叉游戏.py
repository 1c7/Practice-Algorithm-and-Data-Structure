

'''
Data Structures and Algorithms in Python



'''
# 正确创建多维数组
c = 3
r = 3
data = [ [0] * c for j in range(r) ]

print(data)




#
# 实现 3X3的 画圈圈画叉叉游戏
#

'''
# 最后应该这样用：

game = TicTacToe()


# X moves: # O moves:
game.mark(1, 1); game.mark(0, 2)
game.mark(2, 2); game.mark(0, 0)
game.mark(0, 1); game.mark(2, 1)
game.mark(1, 2); game.mark(1, 0)
game.mark(2, 0)


print(game)


winner = game.winner()
if winner is None:
   print( Tie )
 else:
   print(winner, wins )


'''



#
# 开始实现
#


class TicTacToe:

    def init (self):
        self.board = [ [ ] 3 for j in range(3) ]
        self.player = X

    def mark(self, i, j):
 ”””Put an X or O mark at position (i,j) for next player s turn.”””
 if not (0 <= i <= 2 and 0 <= j <= 2):
 raise ValueError( Invalid board position )
 if self. board[i][j] != :
 raise ValueError( Board position occupied )
 if self.winner( ) is not None:
 raise ValueError( Game is already complete )
 self. board[i][j] = self. player
 if self. player == X :
 self. player = O
 else:
 self. player = X
 def is win(self, mark):
 ”””Check whether the board configuration is a win for the given player.”””
 board = self. board # local variable for shorthand
 return (mark == board[0][0] == board[0][1] == board[0][2] or # row 0
 mark == board[1][0] == board[1][1] == board[1][2] or # row 1
 mark == board[2][0] == board[2][1] == board[2][2] or # row 2
 mark == board[0][0] == board[1][0] == board[2][0] or # column 0
 mark == board[0][1] == board[1][1] == board[2][1] or # column 1
 mark == board[0][2] == board[1][2] == board[2][2] or # column 2
 mark == board[0][0] == board[1][1] == board[2][2] or # diagonal
 mark == board[0][2] == board[1][1] == board[2][0]) # rev diag
 def winner(self):
”””Return mark of winning player, or None to indicate a tie.”””
 for mark in XO :
 if self. is win(mark):
 return mark
 return None

 def str (self):
 ”””Return string representation of current game board.”””
 rows = [ | .join(self. board[r]) for r in range(3)]
 return \n-----\n .join(rows)













































