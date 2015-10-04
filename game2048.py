import numpy as np
import numpy.matlib

class gameBoard :
	
	def __init__(self, size) :
		self.score    = 0
		self.size     = size
		self.board    = np.matlib.zeros( (size, size), int, 'F' )

	def readRow(self, row) :
		return self.board[row,:]

	def readCol(self, col) :
		return self.board[:,col]

	def findFirstZero(self, row) :
		for i in range(self.size) :
			if self.board[row, i] != 0 :
				return i
		return 0

	def makeMove(self, moveDirection) :

		# 1 --> Left ::: 2 --> Up ::: 3 --> Down ::: 4 --> Right

		if (moveDirection == 1) : 
			
			for line in range(self.size):
				shift = self.findFirstZero(line) 
				
				if shift :
					for col in range(shift, self.size, 1):
						self.board[line, col - shift], self.board[line, col] = self.board[line, col], 0
				else :
					continue





