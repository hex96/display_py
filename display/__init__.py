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
				temp.append([' ', 0, 0, 0])
			
			self.grid.append(temp)
			
		self.display()
	
	def display(self):
		console.clear()
		
		start_time = datetime.datetime.now()
		
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				r = self.grid[i][j][1]
				g = self.grid[i][j][2]
				b = self.grid[i][j][3]

				console.set_color(r, g, b)
				
				print(self.grid[i][j][0], end='')
				console.set_color()
			
			print()
		
		return datetime.datetime.now() - start_time
	
	def set_pos(self, x, y, char, r=0, g=0, b=0):
		x, y = y, x
		
		if len(char) > 1:
			raise Exception('char too long')
		
		self.grid[x-1][y-1][0] = char
		self.grid[x-1][y-1][1] = r
		self.grid[x-1][y-1][2] = g
		self.grid[x-1][y-1][3] = b
	
	def fill(self, char=' ', r=0, g=0, b=0):
		if len(char) > 1:
			raise Exception('char too long')
		
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				self.grid[i][j][0] = char
				self.grid[i][j][1] = r
				self.grid[i][j][2] = g
				self.grid[i][j][3] = b
