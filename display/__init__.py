import console
import datetime

class Window:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
		self.grid = []
		
		for i in range(self.height):
			temp = []
			for j in range(self.width):
				temp.append(' ')
			
			self.grid.append(temp)
			
		self.display()
	
	def display(self):
		console.clear()
		
		start_time = datetime.datetime.now()
		
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				print(self.grid[i][j], end='')
			
			print()
		
		return datetime.datetime.now() - start_time
	
	def set_pos(self, x, y, char):
		x, y = y, x
		
		if len(char) > 1:
			raise Exception('char too long')
		
		self.grid[x-1][y-1] = char
	
	def fill(self, char=' '):
		if len(char) > 1:
			raise Exception('char too long')
		
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				self.grid[i][j] = char
