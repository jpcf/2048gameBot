import game2048 as g

b = g.gameBoard(4)

b.board[0,1] = 2
b.board[0,2] = 2
b.board[1,2] = 4
b.board[2,0] = 4
b.board[2,1] = 4
b.board[3,3] = 2

print(b.board)

b.makeMove(1)

print(b.board)


