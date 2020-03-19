import display
import time
import random
import _thread

FPS = 100

win = display.Window(5, 5)

x = 1
y = 1

dir = [0, 0]

while True:
	time.sleep(1 / FPS)
	win.fill('x')
	
	win.set_pos(x, y, 'h')
	
	dir = [0, 0]
	
	i = input('')
	if i == 'w':
		dir = [0, -1]
	elif i == 'a':
		dir = [-1, 0]
	elif i == 's':
		dir = [0, 1]
	elif i == 'd':
		dir = [1, 0]
	
	x += dir[0]
	y += dir[1]
	
	if x == win.width:
		x = 0
	elif x == -1:
		x = win.width - 1
	
	if y == win.height:
		y = 0
	elif y == -1:
		y = win.height - 1
	
	
	win.display()
	print(f'\nFPS:{FPS}')
