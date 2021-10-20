from itertools import groupby,chain 

NONE=','
RED='R'
YELLOW='Y'
def positiveDiagonal(matrix,columns,rows): """Get positive-diagonals, going from bottom-left to top-right."""
	for di in ([(j,i-j) for j in range(columns)] for i in range(columns+rows-1)):
		yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < columns and j < rows]

def negativeDiagonal (matrix,columns,rows):
	"""Get negative-diagonals, going from top-left to bottom-right."""
	for di in ([(j, i - columns + j + 1) for j in range(columns)] for i in range(columns + rows - 1)):
		yield [matrix[i][j] for i, j in di if i >= 0 and j >= 0 and i < columns and j < rows]

class GameC4:
	def __init__ (self,columns=7,rows=6,requiredToWin=4):
		"""Create a new GameC4."""
		self.columns=columns
		self.rows=rows
		self.win=requiredToWin
		self.board=[[NONE]*rows for _ in range(columns)]
	def insertColor(self,column,color):
		""" function to insertColor the color(R/Y) in the columns"""
		c= self.board[column]
		if c[0] != NONE:
			raise Exception('Column is full')  #Exception if the colume is full, then it will check the winner
		i = -1
		while c[i]!= NONE:
			i -= 1
		c[i]=color
		self.checkForWin()#calls the fucntion to check winner

	def checkForWin (self):"""Function to check the winner of the GameC4 """
		w = self.getWinner()
		if w:
			self.printGameBoard()
			raise Exception(w + ' won!')

	def getWinner(self):"""Fucntion to get the winner on board"""
		lines=(
			self.board, #columns
			zip(*self.board), #rows
			positiveDiagonal(self.board, self.columns, self.rows), #positive-diagonals
			negativeDiagonal(self.board, self.columns, self.rows) # negative-diagonals
		)
		for line in chain(*lines):
			for color,group in groupby(line):
				if color!= NONE and len(list(group))>= self.win:         
					return color

	def printGameBoard(self):"""Prints the GameC4 board"""
		print('  '.join(map(str, range(self.columns))))
		for y in range(self.rows):
			print('  '.join(str(self.board[x][y]) for x in range(self.columns)))
		print()


if __name__ == '__main__':
	g=GameC4()
	turn=RED
	while True:
		g.printGameBoard()
		row=input('{}\'s turn: '.format('Red' if turn == RED else 'Yellow'))
		g.insertColor(int(row), turn)
		turn=YELLOW if turn==RED else RED
 
